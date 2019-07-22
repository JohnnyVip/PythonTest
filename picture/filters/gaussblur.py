#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
#从指定的目录去找,直接import默认从系统path去找
from picture.filters import boxblur

import time

#import boxblur

from . import boxblur

from picture.filters import boxblur

from ..filters import boxblur

#from .. import filters.boxblur as boxblur

'''

#下面皆为正确示例

from . import boxblur

from ..filters import boxblur

from picture.filters import boxblur

from .boxblur import func

boxblur.func()