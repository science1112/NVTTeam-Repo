import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,random
from t0mm0.common.addon import Addon
from metahandler import metahandlers
from t0mm0.common.net import Net


addon_id = 'plugin.video.hdseries'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
icon2 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/tv.png'))
icon3 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/movies.png'))
icon4 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/search.png'))
icon5 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/play.png'))
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/art/'))
metaset = selfAddon.getSetting('enable_meta')
addon = Addon(addon_id, sys.argv)
net = Net()
basepage = "/date/1"
baseurl2 = "http://www.vodlockerx.com"
def CATEGORIES():
        addDir2('[COLOR yellow]Zadnje TV Oddaje [/COLOR]','http://www.vodlockerx.com/tv-shows/date/1',1,icon2,fanart)
        addDir2('[COLOR lime]Zadnji Filmi [/COLOR]','http://www.vodlockerx.com/movies/date/1',3,icon3,fanart)
        addDir2('(TV Oddaje) Zvrst','http://www.vodlockerx.com/movies/date/1',10,icon2,fanart)

        addDir2('(Filmi) Zvrst','http://www.vodlockerx.com/movies/date/1',11,icon3,fanart)

        addDir2('[COLOR red]>>> Iskanje TV Oddaj [/COLOR]','http://www.vodlockerx.com/tv-shows',4,icon4,fanart)

        addDir2('[COLOR red]>>> Iskanje Filmov [/COLOR]','http://www.vodlockerx.com/movies',5,icon4,fanart)
		
def CATSHOWS():
        addDir2('Action',baseurl2+'/tv-tags/action'+basepage,1,art+'Action-Movies.png',art+'abstract.jpg','')
        addDir2('Adventure',baseurl2+'/tv-tags/adventure'+basepage,1,art+'Adventure-Movies.png',art+'abstract.jpg','')
        addDir2('Animation',baseurl2+'/tv-tags/animation'+basepage,1,art+'Animated-Movies.png',art+'abstract.jpg','')
        addDir2('Biography',baseurl2+'/tv-tags/biography'+basepage,1,art+'Biography-movies.png',art+'abstract.jpg','')
        addDir2('Comedy',baseurl2+'/tv-tags/comedy'+basepage,1,art+'Comedy-Movies.png',art+'abstract.jpg','')
        addDir2('Crime',baseurl2+'/tv-tags/crime'+basepage,1,art+'Crime-Movies.png',art+'abstract.jpg','')
        addDir2('Documentary',baseurl2+'/tv-tags/documentary'+basepage,1,art+'Documentaries.png',art+'abstract.jpg','')
        addDir2('Drama',baseurl2+'/tv-tags/drama'+basepage,1,art+'Drama-Movies.png',art+'abstract.jpg','')
        addDir2('Family',baseurl2+'/tv-tags/family'+basepage,1,art+'Family-Movies.png',art+'abstract.jpg','')
        addDir2('Fantasy',baseurl2+'//tv-tags/fantasy'+basepage,1,art+'Fantasy-Movies.png',art+'abstract.jpg','')
        addDir2('History',baseurl2+'/tv-tags/history'+basepage,1,art+'Historic-Movies.png',art+'abstract.jpg','')
        addDir2('Horror',baseurl2+'/tv-tags/horror'+basepage,1,art+'Horror-Movies.png',art+'abstract.jpg','')
        addDir2('Music',baseurl2+'/tv-tags/music'+basepage,1,art+'Music-icon.png',art+'abstract.jpg','')
        addDir2('Musical',baseurl2+'/tv-tags/musical'+basepage,1,art+'Musical-Movies.png',art+'abstract.jpg','')
        addDir2('Mystery',baseurl2+'/tv-tags/mystery'+basepage,1,art+'Mystery-Movies.ico',art+'abstract.jpg','')
        addDir2('Romance',baseurl2+'/tv-tags/romance'+basepage,1,art+'Romantic-Movies.png',art+'abstract.jpg','')
        addDir2('Sci-Fi',baseurl2+'/tv-tags/sci-fi'+basepage,1,art+'Sci-Fi-Movies.png',art+'abstract.jpg','')
        addDir2('Short',baseurl2+'/tv-tags/short'+basepage,1,art+'Short-Film-movies.Png',art+'abstract.jpg','')
        addDir2('Sport',baseurl2+'/tv-tags/sport'+basepage,1,art+'Sports-Movies.png',art+'abstract.jpg','')
        addDir2('Thriller',baseurl2+'/tv-tags/thriller'+basepage,1,art+'Thriller-Movies.png',art+'abstract.jpg','')
        addDir2('War',baseurl2+'/tv-tags/war'+basepage,1,art+'War-Movies.png',art+'abstract.jpg','')
        addDir2('Western',baseurl2+'/tv-tags/western'+basepage,1,art+'Western-Movies.png',art+'abstract.jpg','')

def CATMOVIES():
        addDir2('Action',baseurl2+'/movie-tags/action'+basepage,1,art+'Action-Movies.png',art+'abstract.jpg','')
        addDir2('Adventure',baseurl2+'/movie-tags/adventure'+basepage,1,art+'Adventure-Movies.png',art+'abstract.jpg','')
        addDir2('Animation',baseurl2+'/movie-tags/animation'+basepage,1,art+'Animated-Movies.png',art+'abstract.jpg','')
        addDir2('Biography',baseurl2+'/movie-tags/biography'+basepage,1,art+'Biography-movies.png',art+'abstract.jpg','')
        addDir2('Comedy',baseurl2+'/movie-tags/comedy'+basepage,1,art+'Comedy-Movies.png',art+'abstract.jpg','')
        addDir2('Crime',baseurl2+'/movie-tags/crime'+basepage,1,art+'Crime-Movies.png',art+'abstract.jpg','')
        addDir2('Documentary',baseurl2+'/movie-tags/documentary'+basepage,1,art+'Documentaries.png',art+'abstract.jpg','')
        addDir2('Drama',baseurl2+'/movie-tags/drama'+basepage,1,art+'Drama-Movies.png',art+'abstract.jpg','')
        addDir2('Family',baseurl2+'/movie-tags/family'+basepage,1,art+'Family-Movies.png',art+'abstract.jpg','')
        addDir2('Fantasy',baseurl2+'//movie-tags/fantasy'+basepage,1,art+'Fantasy-Movies.png',art+'abstract.jpg','')
        addDir2('History',baseurl2+'/movie-tags/history'+basepage,1,art+'Historic-Movies.png',art+'abstract.jpg','')
        addDir2('Horror',baseurl2+'/movie-tags/horror'+basepage,1,art+'Horror-Movies.png',art+'abstract.jpg','')
        addDir2('Music',baseurl2+'/movie-tags/music'+basepage,1,art+'Music-icon.png',art+'abstract.jpg','')
        addDir2('Musical',baseurl2+'/movie-tags/musical'+basepage,1,art+'Musical-Movies.png',art+'abstract.jpg','')
        addDir2('Mystery',baseurl2+'/movie-tags/mystery'+basepage,1,art+'Mystery-Movies.ico',art+'abstract.jpg','')
        addDir2('Romance',baseurl2+'/movie-tags/romance'+basepage,1,art+'Romantic-Movies.png',art+'abstract.jpg','')
        addDir2('Sci-Fi',baseurl2+'/movie-tags/sci-fi'+basepage,1,art+'Sci-Fi-Movies.png',art+'abstract.jpg','')
        addDir2('Short',baseurl2+'/movie-tags/short'+basepage,1,art+'Short-Film-movies.Png',art+'abstract.jpg','')
        addDir2('Sport',baseurl2+'/movie-tags/sport'+basepage,1,art+'Sports-Movies.png',art+'abstract.jpg','')
        addDir2('Thriller',baseurl2+'/movie-tags/thriller'+basepage,1,art+'Thriller-Movies.png',art+'abstract.jpg','')
        addDir2('War',baseurl2+'/movie-tags/war'+basepage,1,art+'War-Movies.png',art+'abstract.jpg','')
        addDir2('Western',baseurl2+'/movie-tags/western'+basepage,1,art+'Western-Movies.png',art+'abstract.jpg','')
		
def GETINDEXMOVIES(url,name):
	try:
			actualpage = str(url)
			
			pagenum = actualpage.split('date/')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'date/'+str(nextpage)
	except:pass
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a class="link" href="(.+?)" title="(.+?)">').findall(link)
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        
        
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                
                if metaset=='false':
                        try:
                                addDir2(name,url,99,iconimage,fanart)
                        except:pass
                else:
                        try:
                                addDir(name,url,99,iconimage,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NASLEDNJI >>',nextpageurl,3,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')	
def GETINDEX(url,name):
	try:
			actualpage = str(url)
			
			pagenum = actualpage.split('date/')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'date/'+str(nextpage)
	except:pass
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a class="link" href="(.+?)" title="(.+?)">').findall(link)
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        
        
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                
                if metaset=='false':
                        try:
                                addDir2(name,url,2,iconimage,fanart)
                        except:pass
                else:
                        try:
                                addDir(name,url,2,iconimage,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GETSEASONS(url,name,iconimage):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        iconimage = iconimage
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a class="link" href="(.+?)" title="(.+?)">').findall(link)
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        
        
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
               
                if metaset=='false':
                        try:
                                addDir2(name,url,99,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir2(name,url,99,icon5,fanart)
                        except:pass
	try:
               
					addLink('NASLEDNJI >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')


		
def GETLINKS(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link=open_url(url)
        match=re.compile('<li class=".+?" style=".+?"><a href="(.+?)" target=".+?">.+?</a></li>').findall(link)
        
        name = name
        for url in match:
                
                
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name +' @ ' + host ,url,100,icon5,fanart)



	
	
	
	
	# ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH -------------------------------------------------------- 
def SEARCH():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search Shows')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','-')
    if len(search_entered)>1:
    
    	url = 'http://www.vodlockerx.com/show/' + search_entered
        link = open_url(url)

        GETSEASONS(url,name,iconimage)

def SEARCHMOVIES():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search Movies')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
    
    	url = 'http://www.vodlockerx.com/index.php?menu=search&query=' + search_entered
        match=re.compile('<a class="link" href="(.+?)" title="(.+?)">').findall(net.http_GET(url).content) 
        for url,name in match:
                        ok = '/movie'
                        if ok in url:
                                name = name.encode('ascii', 'ignore')
                                addDir(name,url,99,iconimage,len(match),isFolder=True)

		
def PLAYLINK(name,url,iconimage):
    try:
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Cannot play the link![/B][/COLOR],[COLOR lime][B]Try another one from the list!![/B][/COLOR],2000,"")")
    addLink('Press Here to Exit','',1,iconimage,fanart)
       
        
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                               
        return param

def addDir2(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        liz.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
        try:
          if not 'COLOR' in name:
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
          
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
            liz.setInfo( type="Video", infoLabels= meta )
            liz.setProperty("IsPlayable","true")
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=False)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
            return ok


		   
        except:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok
        
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if selfAddon.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
print params

if mode==None or url==None or len(url)<1: CATEGORIES()

elif mode==1: GETINDEX(url,name)
elif mode==3: GETINDEXMOVIES(url,name)
elif mode==4: SEARCH()
elif mode==5: SEARCHMOVIES()
elif mode==2: GETSEASONS(url,name,iconimage)
elif mode==10: CATSHOWS()
elif mode==11: CATMOVIES()
elif mode==99: GETLINKS(url,name,iconimage)
elif mode==100: PLAYLINK(name,url,iconimage)


xbmcplugin.endOfDirectory(int(sys.argv[1]))

