# coding:utf-8

from wexy import Wexy
from wsgiref.util import setup_testing_defaults


def test_defaults():
    env = {}
    setup_testing_defaults(env)
