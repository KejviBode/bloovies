'''
This python script will scrape from letterboxd the most popular films this week
'''
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime

from extract_functions import load_letterboxd_soup


WEEKLY_LETTERBOXD_URL = "https://letterboxd.com/films/popular/this/week/year/2023/"
BASE_LETTERBOXD_URL = "https://letterboxd.com"


# def load_top_letterboxd_soup(letterboxd_url: str = WEEKLY_LETTERBOXD_URL,
#                              page_num: int = None) -> BeautifulSoup:
#     '''
#     Load BeautifulSoup from specified letterboxd url
#     '''
#     try:
#         if page_num is None:
#             url = f'{letterboxd_url}'
#         else:
#             url = f'{letterboxd_url}{page_num}'
#         print(f"Retrieving information for: {url}")
#         req = Request(url=url,
#                       headers={'User-Agent': 'Mozilla/5.0'})
#         with urlopen(req) as page:
#             html_bytes = page.read()
#             html = html_bytes.decode("utf-8")
#             soup = BeautifulSoup(html, "html.parser")
#             return soup
#     except HTTPError as err:
#         return {"error": True,
#                 "code": err.code,
#                 "message": err}


if __name__ == "__main__":
    print("Yyyyyello")
    soup = load_letterboxd_soup(WEEKLY_LETTERBOXD_URL)
