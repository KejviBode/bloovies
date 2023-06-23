'''
Helper functions for scraping from letterboxd
'''
import os
import sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

TOP_CHARTS_LETTERBOXD_URL = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/"

def load_letterboxd_soup(letterboxd_url: str = TOP_CHARTS_LETTERBOXD_URL,
                             page_num: int = None) -> BeautifulSoup:
    '''
    Load BeautifulSoup from specified letterboxd_url
    '''
    try:
        if page_num is None:
            url = f'{letterboxd_url}'
        else:
            url = f'{letterboxd_url}{page_num}'
        print(f"Retrieving information for: {url}")
        req = Request(url=url,
                      headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as page:
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            return soup
    except HTTPError as err:
        return {"error": True,
                "code": err.code,
                "message": err}
