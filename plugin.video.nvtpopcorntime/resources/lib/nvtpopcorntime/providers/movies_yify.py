#!/usr/bin/python
import os, sys
from nvtpopcorntime import settings
__addon__ = sys.modules['__main__'].__addon__

_genres = {
    '30400': 'Action',
    '30401': 'Adventure',
    '30402': 'Animation',
    '30403': 'Biography',
    '30404': 'Comedy',
    '30405': 'Crime',
    '30406': 'Documentary',
    '30407': 'Drama',
    '30408': 'Family',
    '30409': 'Fantasy',
    '30410': 'Film-Noir',
    '30411': 'History',
    '30412': 'Horror',
    '30413': 'Music',
    '30414': 'Musical',
    '30415': 'Mystery',
    '30416': 'Romance',
    '30417': 'Sci-Fi',
    '30418': 'Sport',
    '30419': 'Thriller',
    '30420': 'War',
    '30421': 'Western'
}
_proxy_identifier = 'movies.yify.proxies'
def _getDomains():
    domains = [
        "https://yts.ag",
        "http://eqwww.image.yt"
    ]

    # User domains have highest priority
    return settings.movies.proxies+domains

def _create_item(data):
    if not data.get("title"): # Title is require
        return {}

    # Do not return movies without hash, quality and size (require)
    torrents = {}
    for torrent in data.get("torrents", []):
        if torrent.get("quality") and torrent.get("hash") and torrent.get("size_bytes") and torrent["quality"] in settings.QUALITIES:
            torrents[torrent["quality"]] = torrent["hash"]
            torrents['%ssize' %torrent["quality"]] = torrent["size_bytes"]

    if not torrents:
        return {}

    # Set video width and hight
    width = 1920
    height = 1080
    if not torrents.get('1080p'):
        width = 1280
        height = 720

    title = data["title"]
    return {
        "label": title,
        "icon": data.get("medium_cover_image", data.get("small_cover_image")),
        "thumbnail": data.get("medium_cover_image", data.get("small_cover_image")),
        "info": {
            "title": title,
            "year": int(data.get("year") or 0),
            "genre": u" / ".join(genre for genre in data.get("genres", [])) or None,
            "duration": int(data.get("runtime") or 0),
            "code": data.get("imdb_code")
        },
        "properties": {
            "fanart_image": data.get("background_image")
        },
        "stream_info": {
            "video": {
                "codec": u"h264",
                "duration": int((data.get("runtime") or 0)*60),
                "width": width,
                "height": height
            },
            "audio": {
                "codec": u"aac",
                "language": u"en",
                "channels": 2
            }
        },
        "params": torrents
    }

def folders(action, **kwargs):
    '''folders are used to create a list of selection - for example, a catalog of genres

       :param action: (string) When index is call, this parameter will be empty, then set an operation.
       :param kwargs: (dict) When index is call, this parameter will be empty, then contains the user parameters.
       :return: (list) Return a list with items. (Only the first item are used when index is call.)
    '''
    if action == 'genres':
        items= []
        for n in __addon__.getLocalizedString(30499).split(','):
            if _genres.get(n):
                path = os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres', '%s.png' %_genres[n])
                items.append({
                    "label": __addon__.getLocalizedString(int(n)),                      # "label" is require
                    "icon": path,
                    "thumbnail": path,
                    "params": {
                        "endpoint": "browse",                                           # "endpoint" is require
                        'action': "genre",                                              # Require when calling browse or folders (Action is used to separate the content)
                        'genre': _genres[n]                                             # Add user parameter
                    }
                })
        return items

    if action == 'cat':
        return [
            {
                "label": __addon__.getLocalizedString(30002),                       # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "params": {
                    "endpoint": "search"                                            # "endpoint" is require
                }
            },
            {
                "label": __addon__.getLocalizedString(30004),                       # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'popular.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'popular.png'),
                "params": {
                    "endpoint": "browse",                                           # "endpoint" is require
                    'action': "seeds"                                               # Require when calling browse or folders (Action is used to separate the content)
                }
            },
            {
                "label": __addon__.getLocalizedString(30006),                       # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'recently.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'recently.png'),
                "params": {
                    "endpoint": "browse",                                           # "endpoint" is require
                    'action': "date_added"                                          # Require when calling browse or folders (Action is used to separate the content)
                }
            },
            {
                "label": __addon__.getLocalizedString(30005),                       # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "endpoint": "browse",                                           # "endpoint" is require
                    'action': "rating"                                              # Require when calling browse or folders (Action is used to separate the content)
                }
            },
            {
                "label": __addon__.getLocalizedString(30003),                       # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "params": {
                    "endpoint": "folders",                                          # "endpoint" is require
                    'action': "genres"                                              # Require when calling browse or folders (Action is used to separate the content)
                }
            }
        ]

    # There was no action, therefore has index be called  
    return [{
        "label": __addon__.getLocalizedString(30030),                               # "label" is require
        "icon": os.path.join(settings.addon.resources_path, 'media', 'movies.png'),
        "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies.png'),
        "params": {
            "endpoint": "folders",                                                  # "endpoint" is require
            'action': "cat"                                                         # Require when calling browse or folders (Action is used to separate the content)
        }
    }]

def browse(action, page, **kwargs):
    '''browse are used to returning parameters used for 'Request' when a movie list is displayed.

       :param action: (string) This parameter set an operation
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters
       :return: (dict) Return parameters used for 'Request'
    '''
    return {
        'proxies': _getDomains(),
        'path': "/api/v2/list_movies.json",
        'params': {
            'limit': settings.addon.limit, # Do not return more media end the limit, only lees (require)
            'page': page,
            'quality': 'all',
            'genre': action == 'genre' and kwargs['genre'] or 'all',
            'sort_by': action == 'genre' and "seeds" or action,
            'order_by': 'desc',
        },
        'proxyid': _proxy_identifier
    }

def browse_build(data, action, page, **kwargs):
    '''browse_build are used to create a dict with the items when a movie list is displayed.

       :param data: Contains a list with data from 'Request'
       :param action: (string) This parameter set an operation
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters that were given to browse function
       :return: Return a dict
    '''
    if not data or int(data.get("data", {}).get("movie_count", 0)) <= 0:
        return {}

    items = []
    for movie in data["data"]["movies"]:
        item = _create_item(movie)
        if item:
            items.append(item)

    if not items:
        return {}

    movie_count = int(data.get("data", {}).get("movie_count", 20))
    return {
        'pages': int(movie_count/settings.addon.limit) + (movie_count%settings.addon.limit > 0), # Specify the total number of pages (require)
        'items': items
    }

def search(query, page, **kwargs):
    '''search are used to returning parameters used for 'Request' when a search result is displayed.

       :param query: (string) Contains an query string
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters
       :return: (dict) Return parameters used for 'Request'
    '''
    return {
        'proxies': _getDomains(),
        'path': "/api/v2/list_movies.json",
        'params': {
            'limit': settings.addon.limit, # Do not return more media end the limit, only lees
            'page': page,
            'quality': 'all',
            'query_term': query.encode('UTF-8')
        },
        'proxyid': _proxy_identifier
    }

def search_build(data, query, page, **kwargs):
    '''search_build are used to create a dict with the items when a search result is displayed.

       :param data: Contains a list with data from 'Request'
       :param query: (string) Contains an query string
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters that were given to search function
       :return: Return a dict
    '''
    if not data or int(data.get("data", {}).get("movie_count", 0)) <= 0:
        return {}

    items = []
    for movie in data["data"]["movies"]:
        item = _create_item(movie)
        if item:
            items.append(item)

    if not items:
        return {}

    movie_count = int(data.get("data", {}).get("movie_count", 20))
    return {
        'pages': int(movie_count/settings.addon.limit) + (movie_count%settings.addon.limit > 0), # Specify the total number of pages (require)
        'items': items
    }
