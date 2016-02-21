# coding:utf-8

from wexy import Wexy
from wsgiref.util import setup_testing_defaults


def test_defaults():
    env = {}
    setup_testing_defaults(env)
    print env
    w = Wexy(env)

    assert w.request_method == 'GET'
    assert w.path_info == '/'
    assert w.server_name == '127.0.0.1'
    assert w.server_port == '80'
    assert w.server_protocol == 'HTTP/1.0'
    assert w.wsgi_url_scheme == 'http'
    assert w.wsgi_multithread == 0
    assert w.wsgi_multiprocess == 0
    assert w.wsgi_run_once == 0
    assert w.wsgi_version == (1, 0)
    assert w.get_http('host') == '127.0.0.1'
