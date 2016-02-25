'''
    NVTTeam Porn
    Copyright (C) 2015 mortael
    Copyright (C) 2015 Fr40m1nd

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

import urllib, re
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils

progress = utils.progress

def Main():
    utils.addDir('[COLOR yellow]Search[/COLOR]','http://www.mrsexe.com/?search=', 404, '', '')
    utils.addDir('[COLOR yellow]Categories[/COLOR]','http://www.mrsexe.com/', 403, '', '')
    utils.addDir('[COLOR yellow]Stars[/COLOR]','http://www.mrsexe.com/filles/', 405, '', '')
    List('http://www.mrsexe.com/')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml(url, '')
    match = re.compile(r'<a class="thumbnail" href="(.+?)">\n<script.+?</script>\n<figure>\n<img  id=".+?" src="(.+?)".+?/>\n<figcaption>\n<span class="video-icon"><i class="fa fa-play"></i></span>\n<span class="duration"><i class="fa fa-clock-o"></i>(.+?)</span>\n(.+?)\n').findall(listhtml)
    for videopage, img, duration, name in match:
        name = utils.cleantext(name) + ' ' + duration
        utils.addDownLink(name, 'http://www.mrsexe.com/' + videopage, 402, img, '')
    try:
        nextp=re.compile(r'<li class="arrow"><a href="(.+?)">suivant</li>').findall(listhtml)
        utils.addDir('Next Page', 'http://www.mrsexe.com/' + nextp[0], 401,'')
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
    match = re.compile(r'<a href="(/cat/.+?)".+?>(.+?)</a>', re.DOTALL | re.IGNORECASE).findall(cathtml)
    for catpage, name in match:
        utils.addDir(name, 'http://www.mrsexe.com/' + catpage, 401, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Stars(url):
    print "mrsexe::Stars " + url
    starhtml = utils.getHtml(url, '')
    match = re.compile(r'<figure>\s<a href="(.+?)"><img src="(.+?)" alt=""\s/></a>\s</figure>.+?</div>\s<div class="infos">\s<h5><a href=".+?">([\w\s]+)</a></h5>\s([0-9]+) vid', re.DOTALL | re.IGNORECASE).findall(starhtml)
    for starpage, img, name, vidcount in match:
        name = name + " (" + vidcount + " Videos)"
        utils.addDir(name, 'http://www.mrsexe.com/' + starpage, 401, img)
    try:
        nextp=re.compile(r'<li class="arrow"><a href="(.+?)">suivant</li>').findall(starhtml)
        utils.addDir('Next Page', 'http://www.mrsexe.com/' + nextp[0], 405,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Playvid(url, name, download=None):
    print "mrsexe::Playvid " + url
    html = utils.getHtml(url, '')
    videourl = re.compile(r"src='(/inc/clic\.php\?video=.+?&cat=mrsex.+?)'").findall(html)
    html = utils.getHtml('http://www.mrsexe.com/' + videourl[0], '')
    videourls = re.compile(r"'file': \"(.+?)\",.+?'label': '(.+?)'", re.DOTALL).findall(html)
    videourls = sorted(videourls, key=lambda tup: tup[1], reverse=True)
    videourl = videourls[0][0]
    if download == 1:
        utils.downloadVideo(videourl, name)
    else:    
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Porn'})
        xbmc.Player().play(videourl, listitem)