# omdb.py

import urllib.parse

import requests

OMDB_KEY = 'YOUR_OMDB_KEY'

def get_omdb_results(movies_list):
    """ (list of {movie, year} dicts) -> json

    Get json results for movies_list from omdb

    Returns json search results from omdb"""
    search_data = []

    for m in movies_list:
        encoded_title = urllib.parse.quote_plus(m['title'])
        year = m['year']
        omdb_url = f'http://www.omdbapi.com/?apikey={OMDB_KEY}&t={encoded_title}&y={year}'
        resp = requests.get(omdb_url)
        search_data.append(resp.json())
    print('Data from OMDB obtained successfully')
    return search_data
