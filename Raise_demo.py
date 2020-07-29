#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/10/15 19:30
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : Raise_demo.py
@Software : PyCharm Community
"""

import keyword
import re
from collections import namedtuple
from typing import Sequence, Dict, TypeVar, List, Type, Generic

T = TypeVar('T')


def k2d(*keys):
    return {k: k for k in keys}


def d2d(d: dict, keys: Sequence[str] = None, mapping: Dict[str, str] = None, force_k=False):
    if not keys and not mapping:
        return d

    return {v: d.get(k) for k, v in {**k2d(keys), **mapping}.items() if d.get(k) or force_k}


def any_to_tuple(data, typename='_'):
    if isinstance(data, list):
        return [any_to_tuple(data=x, typename=typename) for x in data]
    elif isinstance(data, dict):
        if first(list(data.keys()), lambda x: re.fullmatch('\\d+(.\\d+)?', str(x))):
            return {k: any_to_tuple(v, k) for k, v in data.items()}
        else:
            _keys = data.keys() - set(keyword.kwlist)
            _tpl = namedtuple(typename=typename, field_names=_keys)
            _data = {k: any_to_tuple(data.get(k), k) for k in _keys}
            return _tpl(**_data)
    else:
        return data


def any_to_dict(data):
    if data and isinstance(data, list):
        return [any_to_dict(x) for x in data]
    elif data and isinstance(data, dict):
        return {k: any_to_dict(v) for k, v in data.items()}
    elif data and isinstance(data, tuple):
        if hasattr(data, '__annotations__'):
            return {k: any_to_dict(getattr(data, k)) for k in data.__annotations__.keys()}
        elif hasattr(data, '_fields'):
            return {k: any_to_dict(getattr(data, k)) for k in getattr(data, '_fields')}
        else:
            print('any_to_dict', 'tuple', '???', dir(data))
            return data
    else:
        return data


def diff_dict(a: dict, b: dict, keys: Sequence[str] = None):
    if keys:
        return dict(d2d(a, keys).items() - d2d(b, keys).items())
    return dict(a.items() - b.items())


def diff_list(a: List[T], b: List[T]) -> List[T]:
    if not a:
        return []

    _b = b if b else []
    return [x for x in a if x not in _b]


def first(seq: Sequence[T], p) -> T:
    for x in seq:
        if p(x):
            return x

    return None


def last(seq: Sequence[T], p) -> T:
    n = len(seq)
    while n:
        n -= 1
        x = seq[n]
        if p(x):
            return x

    return None


def cast_data(data, t: Type[T] = any) -> T:
    if data is None:
        return None

    if t is None or t == any:
        if isinstance(data, list):
            return [D(**x) if isinstance(x, dict) else x for x in data]
        elif isinstance(data, dict):
            return D(**data)
        else:
            return data

    _m = getattr(t, '__module__', None)
    _o = getattr(t, '__origin__', None)
    if _m == 'builtins':
        if t == object:
            return data
        elif t in (str, int, float):
            return t(data)
        elif t == bool:
            if isinstance(data, str):
                return data.lower() == 'true'
            elif isinstance(data, (int, float)):
                return data != 0
            else:
                return bool(data)
        else:
            print('unhandled', _m, t)
            return data

    elif _m == 'typing':
        _a = getattr(t, '__args__', tuple({}))

        if _o == list:
            return [cast_data(x, _a[0]) for x in data]
        elif _o == dict:
            return {k: cast_data(data.get(k), _a[-1]) for k in data.keys()}
        elif issubclass(t, List):
            return [cast_data(x, _a[0]) for x in data]
        elif issubclass(t, D):
            return t(**data)
        else:
            print('unhandled', _m, t)
            return data

    elif _o == R:
        _a = getattr(t, '__args__', tuple({}))
        return R(data, t=_a[0])

    elif issubclass(t, (C, D)):
        return t(**data)

    else:
        print('unhandled', _m, t)
        return data


class D(Dict):
    def __init__(self, **kwargs):
        super().__init__()

        _annotations = getattr(self, '__annotations__', None)

        for k, v in kwargs.items():
            _t = _annotations.get(k) if _annotations else None
            self.__setitem__(k, cast_data(v, _t))

        if _annotations:
            for k in [x for x in _annotations.keys() if x not in kwargs.keys()]:
                self.__setitem__(k, getattr(self, k, None))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            raise

    def __getattr__(self, k, v=None):
        return self.__getitem__(k) if k in self.keys() else v

    def has(self, k):
        return k in self.keys()


class C(D):
    def __getattr__(self, k, v=None):
        _k = list(filter(lambda x: x.lower() == k.lower(), self.keys()))

        return self.__getitem__(_k[0]) if _k else v

    def has(self, k):
        return k.lower() in [x.lower() for x in self.keys()]


class R(Generic[T]):
    code: int = 0
    message: str = None
    result: T = None

    def __init__(self, m: dict, t: Type[T]):
        self.code = m.get('code', 0)
        self.message = m.get('message', None)
        self.result = cast_data(m.get('result', None), t)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            raise
