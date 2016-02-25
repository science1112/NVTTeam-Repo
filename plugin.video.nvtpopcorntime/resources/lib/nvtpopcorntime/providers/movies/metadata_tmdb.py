#!/usr/bin/python
import time
from nvtpopcorntime.utils import Cache

FALLBACKLANG = 'en' # Or None

_api_key = "308a68c313ff66d165c1eb029b0716bc"
_base_url = "http://api.themoviedb.org"
_images_base_url = None

class _Data():
    _limit     = 40
    _timelimit = 10
    _count     = 0
    _time      = 0
    imageUrl   = None

    @staticmethod
    def limit():
        if not _Data._time:
            _Data._time = time.time()

        _timediff = time.time()-_Data._time
        if _Data._count >= _Data._limit:
            while _timediff < _Data._timelimit:
                print('sleep')
                time.sleep(_timediff)
                _timediff = time.time()-_Data._time
        if _timediff >= _Data._timelimit:
            _Data._count = 0
            _Data._time = time.time()

        _Data._count = _Data._count+1

def _credits(credits):
    castandrole = []
    director = []
    writer = []

    for c in credits.get("cast", []):
        castandrole.append((c["name"], c.get("character", '')))

    for c in credits.get("crew", []):
        if c["job"] == 'Director':
            director.append(c["name"])
            continue
        if c["job"] == 'Novel' or c["job"] == 'Writer' or c["job"] == 'Screenplay':
            writer.append(c["name"])

    return {
        'castandrole': castandrole,
        'director': u" / ".join(director),
        'writer': u" / ".join(writer)
    }

def _info(meta, title=''):
    overview = meta.get('overview', '')
    vote_average = meta.get('vote_average')
    item = {
        "title": title,
        "year": int(meta.get("release_date", '0').split("-").pop(0)),
        "originaltitle": meta.get("original_title", ''),
        "genre": u" / ".join(g["name"] for g in meta.get("genres", [])),
        "plot": overview,
        "plotoutline": overview,
        "tagline": meta.get("tagline", ''),
        "rating": float(vote_average or 0.0),
        "duration": int(meta.get("runtime") or 0),
        "code": meta.get("imdb_id"),
        "studio": u" / ".join([s['name'] for s in meta.get("production_companies", [])]),
        "votes": vote_average and float(meta.get("vote_count")) or 0.0
    }

    credits = meta.get("credits")
    if credits:
        item.update(_credits(credits))

    return item

def _stream_info(meta):
    return {
        "video": {
            "duration": int((meta.get("runtime") or 0)*60)
        }
    }

def _properties(meta):
    fanart = meta.get("fanart", '')
    if _Data.imageUrl and fanart:
        fanart = "%s/w500%s" %(_Data.imageUrl, fanart)

    return {"fanart_image": fanart}

def pre():
    cache = Cache("movies.metadata.imdb.conf", ttl=24 * 3600, readOnly=True)
    try:
        _Data.imageUrl = cache["imageUrl"]
    except KeyError:
        _Data.limit()
        return [{
            'domain': _base_url,
            'path': "/3/configuration",
            'params':  {
                "api_key": _api_key
            }
        }]
    return []

def build_pre(data):
    if data:
        _Data.imageUrl = data[0].get("images", {}).get("base_url")
        if _Data.imageUrl:
            Cache("movies.metadata.imdb.conf", ttl=24 * 3600)['imageUrl'] = _Data.imageUrl

def item(id, label, year, lang):
    _Data.limit()
    return {
        'domain': _base_url,
        'path': "/3/movie/%s" %id,
        'params':  {
            "api_key": _api_key,
            "append_to_response": "credits",
            "language": lang,
            "include_image_language": "en,null"
        }
    }

def build_item(meta, id, label, year, lang):
    if not meta or meta.get('status_code'):
        return {}

    title = meta.get("title", '')

    poster = meta.get("poster_path", '')
    if _Data.imageUrl and poster:
        poster = "%s/w500%s" %(_Data.imageUrl, poster)

    item = {
        "label": title,
        "icon": poster,
        "thumbnail": poster
    }
    item.setdefault('info', {}).update(_info(meta, title))
    item.setdefault('stream_info', {}).update(_stream_info(meta))
    item.setdefault('properties', {}).update(_properties(meta))

    return item
