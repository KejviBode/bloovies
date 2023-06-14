'''
This python script will scrape from letterboxd
'''
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

TOP_CHARTS_LETTERBOXD_URL = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/"


def load_top_letterboxd_soup(page_num: int, letterboxd_url: str = TOP_CHARTS_LETTERBOXD_URL) -> BeautifulSoup:
    '''
    Load BeautifulSoup from Letterboxd top 250 reviewed films of all time
    '''
    try:
        req = Request(url=f'{letterboxd_url}{page_num}', 
                      headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as page:
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            return soup
    except HTTPError as err:
        return {"error" : True,
                "code" : err.code,
                "message" : err}



if __name__ == "__main__":
    main_soup = load_top_letterboxd_soup(1)
    print(main_soup)
