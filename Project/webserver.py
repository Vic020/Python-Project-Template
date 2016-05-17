# -*- encoding: utf-8 -*-

from __future__ import unicode_literals, absolute_import


from Project.libs.common import Base


class WebServer(Base):
    def __init__(self, **kwargs):
        super(WebServer, self).__init__(**kwargs)

    def run(self):
        self.logger.info("Start")
        pass
        self.logger.info("End")