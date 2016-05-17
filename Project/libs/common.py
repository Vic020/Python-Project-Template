# -*- encoding: utf-8 -*-

import logging


class Base(object):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(kwargs.get('logger', ''))
