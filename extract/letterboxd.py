from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

TOP_CHARTS_LETTERBOXD_URL = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/"


def load_letterboxd_soup(page_num: int, letterboxd_url: str = TOP_CHARTS_LETTERBOXD_URL) -> BeautifulSoup:
    try: 
        req = Request(url=f'{letterboxd_url}{page_num}', headers={'User-Agent' : 'Mozilla/5.0'})
    except:
        return None
    with urlopen(req) as page:
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        return soup



if __name__ == "__main__":
    soup = load_letterboxd_soup(1)
    print(soup.find("h1").find("a").contents[0])