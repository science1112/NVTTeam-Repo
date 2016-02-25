#!/usr/bin/python
import os, sys, xbmc, xbmcplugin, ctypes
from .base import _Base
from nvtpopcorntime.platform import Platform
from nvtpopcorntime.settings import addon as _settings
from nvtpopcorntime.exceptions import Notify, Error
from nvtpopcorntime.logging import log, LOGLEVEL
from nvtpopcorntime.utils import Dialog, notify, NOTIFYLEVEL, build_magnetFromMeta, shortenBytes
from nvtpopcorntime.torrent import TorrentPlayer

__addon__ = sys.modules['__main__'].__addon__

class Player(_Base):
    def calculate_free_space(self):
        if Platform.system == 'android': 
            # http://stackoverflow.com/questions/1749928/replacement-for-python-statvfs#comment42443537_1749950
            # https://github.com/Diblo/KODI-Popcorn-Time/issues/68
            return 16106127360 # 15 GB
        if Platform.system == 'windows':
            free_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(self.mediaSettings.download_path), None, None, ctypes.pointer(free_bytes))
            return free_bytes.value
        st = os.statvfs(self.mediaSettings.download_path)
        return st.f_bavail * st.f_frsize

    def getSelectedItem(self):
        castAndRole = []
        _c = xbmc.getInfoLabel('ListItem.CastAndRole')
        if _c:
            castAndRole = [cr.split(' as ', 1) for cr in _c.replace('\n', ' / ').split(' / ')]

        return {
            "label": xbmc.getInfoLabel('ListItem.Label'),
            "icon": xbmc.getInfoLabel('ListItem.Icon'),
            "thumbnail": xbmc.getInfoLabel('ListItem.Thumb'),
            "info": {
                "title": xbmc.getInfoLabel('ListItem.Title'),
                "year": int(xbmc.getInfoLabel('ListItem.Year') or 0),
                "originaltitle": xbmc.getInfoLabel('ListItem.OriginalTitle'),
                "genre": xbmc.getInfoLabel('ListItem.Genre'),
                'castandrole': castAndRole,
                'director': xbmc.getInfoLabel('ListItem.Director'),
                "plot": xbmc.getInfoLabel('ListItem.Plot'),
                "plotoutline": xbmc.getInfoLabel('ListItem.PlotOutline'),
                "tagline": xbmc.getInfoLabel('ListItem.Tagline'),
                "writer": xbmc.getInfoLabel('ListItem.Writer'),
                "rating": float(xbmc.getInfoLabel('ListItem.Rating') or 0.0),
                "duration": int(xbmc.getInfoLabel('ListItem.Duration') or 0),
                "code": xbmc.getInfoLabel('ListItem.IMDBNumber'),
                "studio": xbmc.getInfoLabel('ListItem.Studio'),
                "votes": xbmc.getInfoLabel('ListItem.Rating') and float(xbmc.getInfoLabel('ListItem.Votes')) or 0.0
            },
            "properties": {
                "fanart_image": xbmc.getInfoLabel("ListItem.Property(fanart_image)")
            },
            "stream_info": {
                "video": {
                    "codec": xbmc.getInfoLabel('ListItem.VideoCodec'),
                    "duration": int(xbmc.getInfoLabel('ListItem.Duration') or 0)*60,
                    "width": int(xbmc.getInfoLabel('ListItem.VideoResolution')),
                    "height": xbmc.getInfoLabel('ListItem.VideoResolution') == '1920' and 1080 or 720
                },
                "audio": {
                    "codec": xbmc.getInfoLabel('ListItem.AudioCodec'),
                    "language": xbmc.getInfoLabel('ListItem.AudioLanguage'),
                    "channels": int(xbmc.getInfoLabel('ListItem.AudioChannels') or 2)
                },
                'subtitle': {
                    'language': xbmc.getInfoLabel('ListItem.SubtitleLanguage')
                }
            }
        }

    def show(self, subtitle=None, quality=None, **params):
        log("(Player) Creating player options")
        if _settings.handle > -1:
            xbmcplugin.endOfDirectory(_settings.handle, True, False, False) # https://github.com/Diblo/KODI-Popcorn-Time/issues/57

        item = self.getSelectedItem()

        free_space = self.calculate_free_space()
        if not quality:
            waring = []
            for _q in self.mediaSettings.qualities:
                if params.get(_q):
                    if params['%ssize' %_q] > free_space:
                        if _q == '3D' and self.mediaSettings.play3d == 1 and not Dialog().yesno(line2=30011, lineStr1=' ', headingStr=item['info']['title']):
                            continue
                        quality = _q
                        break
                    waring = waring+[_q]

            if waring:
                if not quality:
                    raise Notify('There is not enough free space in %s' %self.mediaSettings.download_path, 30323, level=NOTIFYLEVEL.ERROR)

                if len(waring) > 1:
                    notify(message=__addon__.getLocalizedString(30325) %(", ".join(waring), waring.pop()), level=NOTIFYLEVEL.WARNING)
                else:
                    notify(message=__addon__.getLocalizedString(30326) %waring[0], level=NOTIFYLEVEL.WARNING)
                log('(Player) There must be a minimum of %s to play. %s available in %s' %(shortenBytes(params['%ssize' %quality]), shortenBytes(free_space), self.mediaSettings.download_path), LOGLEVEL.NOTICE)

        elif not params.get(quality):
                raise Error('%s quality was not found' %quality, 30023)
        elif params['%ssize' %quality] < free_space:
                raise Notify('There is not enough free space in %s' %self.mediaSettings.download_path, 30323, level=NOTIFYLEVEL.ERROR)

        TorrentPlayer().playTorrentFile(self.mediaSettings, build_magnetFromMeta(params[quality], "quality %s" %quality), item, subtitle)
