#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2014 sorax
#
#  This file is part of the detektor.fm xbmc plugin.
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin.  If not, see <http://www.gnu.org/licenses/>.


from os.path import join
from sys import argv
from time import gmtime, strftime, strptime
from urllib import quote_plus, urlopen
from urlparse import parse_qs, urlparse
from xml.dom.minidom import parseString
from xbmc import translatePath
import xbmcaddon
from xbmcgui import Dialog, ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory

MAXIMAFM_STREAM = 'http://5243.live.streamtheworld.com:80/MAXIMAFM_SC'

#---> [playlist]
# File1=http://13413.live.streamtheworld.com:443/MAXIMAFM_SC
# File2=http://13413.live.streamtheworld.com:3690/MAXIMAFM_SC
# File3=http://13413.live.streamtheworld.com:80/MAXIMAFM_SC
# File4=http://13393.live.streamtheworld.com:443/MAXIMAFM_SC
# File5=http://13393.live.streamtheworld.com:3690/MAXIMAFM_SC
# File6=http://13393.live.streamtheworld.com:80/MAXIMAFM_SC
# File7=http://13873.live.streamtheworld.com:443/MAXIMAFM_SC
# File8=http://13873.live.streamtheworld.com:3690/MAXIMAFM_SC
# File9=http://13873.live.streamtheworld.com:80/MAXIMAFM_SC
# File10=http://10883.live.streamtheworld.com:443/MAXIMAFM_SC
# File11=http://10883.live.streamtheworld.com:3690/MAXIMAFM_SC
# File12=http://10883.live.streamtheworld.com:80/MAXIMAFM_SC
# File13=http://13303.live.streamtheworld.com:443/MAXIMAFM_SC
# File14=http://13303.live.streamtheworld.com:3690/MAXIMAFM_SC
# File15=http://13303.live.streamtheworld.com:80/MAXIMAFM_SC
# File16=http://5293.live.streamtheworld.com:443/MAXIMAFM_SC
# File17=http://5293.live.streamtheworld.com:3690/MAXIMAFM_SC
# File18=http://5293.live.streamtheworld.com:80/MAXIMAFM_SC
# File19=http://10913.live.streamtheworld.com:443/MAXIMAFM_SC
# File20=http://10913.live.streamtheworld.com:3690/MAXIMAFM_SC
# File21=http://10913.live.streamtheworld.com:80/MAXIMAFM_SC
# File22=http://13863.live.streamtheworld.com:443/MAXIMAFM_SC
# File23=http://13863.live.streamtheworld.com:3690/MAXIMAFM_SC
# File24=http://13863.live.streamtheworld.com:80/MAXIMAFM_SC
# File25=http://10923.live.streamtheworld.com:443/MAXIMAFM_SC
# File26=http://10923.live.streamtheworld.com:3690/MAXIMAFM_SC
# File27=http://10923.live.streamtheworld.com:80/MAXIMAFM_SC
# File28=http://13373.live.streamtheworld.com:443/MAXIMAFM_SC
# File29=http://13373.live.streamtheworld.com:3690/MAXIMAFM_SC
# File30=http://13373.live.streamtheworld.com:80/MAXIMAFM_SC
# File31=http://5243.live.streamtheworld.com:443/MAXIMAFM_SC
# File32=http://5243.live.streamtheworld.com:3690/MAXIMAFM_SC
# File33=http://5243.live.streamtheworld.com:80/MAXIMAFM_SC
#Title1=MAXIMAFM_SC
#<---

class StreamPlayer:

    def __init__(self, url):
        self.url = url

    def addLink(self, name, url, image = '', info = {}, totalItems = 0):
        item = ListItem(name.encode('utf-8'), iconImage = image, thumbnailImage = image)
        item.setProperty('mimetype', 'audio/mpeg')
        item.setInfo('music', info)
        return addDirectoryItem(int(argv[1]), url, item, False, totalItems)

    def buildIndex(self):
        self.addLink('[COLOR green][B]Maxima FM[/B][/COLOR] [COLOR blue] LIVE[/COLOR]', self.url, '', {
            'title': 'Maxima FM',
        })

    def run(self, handle):
        endOfDirectory(int(handle))

if __name__ == '__main__':
    kiisfm = StreamPlayer(MAXIMAFM_STREAM)
    kiisfm.buildIndex()
    kiisfm.run(argv[1])
