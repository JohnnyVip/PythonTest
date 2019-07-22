#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class IPBlacklistMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        ip_addr = environ.get('HTTP_HOST').split(':')[0]
        if ip_addr not in ('127.0.0.1'):
            return forbidden(start_response)

        return self.app(environ, start_response)


def dog(start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['This is dog!']


def cat(start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['This is cat!']


def not_found(start_response):
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']


def forbidden(start_response):
    start_response('403 Forbidden', [('Content-Type', 'text/plain')])
    return ['Forbidden']


def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    mapping = {'dog': dog, 'cat': cat}

    call_back = mapping[path] if path in mapping else not_found
    return call_back(start_response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    application = IPBlacklistMiddleware(application)
    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()