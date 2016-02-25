# -*- coding: utf-8 -*-



import re,urlparse
from resources.lib.libraries import client


def resolve(url):
    try:
        id = (urlparse.urlparse(url).path).split('/')[-1]

        result = client.request(url)
        result = result.replace('\r','').replace('\n','').replace('\t','')
        result = result.split('"%s"' % id)[-1].split(']]')[0]

        result = re.compile('\d*,\d*,\d*,"(.+?)"').findall(result)
        result = [i.replace('\\u003d','=').replace('\\u0026','&') for i in result][::-1]
        result = sum([tag(i) for i in result], [])

        url = []
        try: url += [[i for i in result if i['quality'] == '1080p'][0]]
        except: pass
        try: url += [[i for i in result if i['quality'] == 'HD'][0]]
        except: pass
        try: url += [[i for i in result if i['quality'] == 'SD'][0]]
        except: pass

        if url == []: return
        return url
    except:
        return


def tag(url):
    quality = re.compile('itag=(\d*)').findall(url)
    quality += re.compile('=m(\d*)$').findall(url)
    try: quality = quality[0]
    except: return []

    if quality in ['37', '137', '299', '96', '248', '303', '46']:
        return [{'quality': '1080p', 'url': url}]
    elif quality in ['22', '84', '136', '298', '120', '95', '247', '302', '45', '102']:
        return [{'quality': 'HD', 'url': url}]
    elif quality in ['35', '44', '135', '244', '94']:
        return [{'quality': 'SD', 'url': url}]
    elif quality in ['18', '34', '43', '82', '100', '101', '134', '243', '93']:
        return [{'quality': 'SD', 'url': url}]
    elif quality in ['5', '6', '36', '83', '133', '242', '92', '132']:
        return [{'quality': 'SD', 'url': url}]
    else:
        return []


