#!/usr/bin/python
from .base3 import _Base3
from nvtpopcorntime.logging import log, LOGLEVEL

class Season(_Base3):
    def show(self, action, **params):
        log("(Season) Creating view", LOGLEVEL.INFO)
        curPageNum = self.getCurPageNum()
