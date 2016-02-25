#!/usr/bin/python
import sys
from .base2 import _Base2, _MetaClass2, load_provider

__addon__ = sys.modules['__main__'].__addon__

class Tvshows(_Base2):
    class __metaclass__(_MetaClass2):
        def _provider(cls):
            """cls.provider = cls.load_provider('tvshows_xxxx')"""
            cls.provider = None

        def _metadata_provider(cls):
            provider = __addon__.getSetting('tvshows_metadata_provider')
            if not provider == '0':
                _list = []
                cls.metadata_provider = cls.load_provider('tvshows.%s' % _list[int(provider)-1])
            else:
                cls.metadata_provider = None

        def _subtitles_provider(cls):
            provider = __addon__.getSetting('tvshows_subtitle_provider')
            if not provider == '0' and not __addon__.getSetting('tvshows_subtitle_language0') == '0':
                _list = []
                cls.subtitles_provider = cls.load_provider('tvshows.%s' % _list[int(provider)-1])
            else:
                cls.subtitles_provider = None
