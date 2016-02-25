'''
    NVTTeam Porn
    Copyright (C) 2015 mortael
    Copyright (C) 2015 anton40

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import urllib, re, base64
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils

progress = utils.progress

def Main():
    utils.addDir('[COLOR yellow]Search[/COLOR]','http://www.pornhub.com/video/search?o=mr&search=', 394, '', '')
    utils.addDir('[COLOR yellow]Categories[/COLOR]','http://www.pornhub.com/categories', 393, '', '')
    List('http://www.pornhub.com/video?o=cm')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def List(url):
    print "pornhub::List " + url
    listhtml = utils.getHtml(url, '')
    match = re.compile('<li class="videoblock".+?<a href="([^"]+)" title="([^"]+)".+?<var class="duration">([^<]+).*?data-mediumthumb="([^"]+)"', re.DOTALL).findall(listhtml)
    for videopage, name, duration, img in match:
        name = utils.cleantext(name)
        name = name + " [COLOR blue]" + duration + "[/COLOR]"
        utils.addDownLink(name, 'http://www.pornhub.com' + videopage, 392, img, '')
    try:
        nextp=re.compile('<li class="page_next"><a href="(.+?)" class="orangeButton">Next</a></li>', re.DOTALL).findall(listhtml)
        utils.addDir('Next Page', 'http://www.pornhub.com' + nextp[0].replace('&amp;','&'), 391,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Searching for...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','+')
    searchUrl = searchUrl + title
    print "Searching URL: " + searchUrl
    List(searchUrl)

def Categories(url):
    cathtml = utils.getHtml(url, '')
    match = re.compile('<div class="category-wrapper">.+?<a href="(.+?)"  alt="(.+?)">.+?<img src="(.+?)"', re.DOTALL).findall(cathtml)
    for catpage, name, img, in sorted(match, key=lambda item: item[1]):
        if '?' in catpage:
            utils.addDir(name, 'http://www.pornhub.com' + catpage + "&o=cm", 391, img, '')
        else:
            utils.addDir(name, 'http://www.pornhub.com' + catpage + "?o=cm", 391, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Playvid(url, name, download=None):
    html = utils.getHtml(url, '')
    videourl = re.compile("var player_quality_.+? = '(.+?)'").findall(html)
    videourl = videourl[-1]
    if download == 1:
        utils.downloadVideo(videourl, name)
    else:    
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Porn'})
        xbmc.Player().play(videourl, listitem)