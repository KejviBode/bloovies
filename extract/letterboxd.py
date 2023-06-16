'''
This python script will scrape from letterboxd
'''
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

TOP_CHARTS_LETTERBOXD_URL = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/"


def load_top_letterboxd_soup(page_num: int,
                             letterboxd_url: str = TOP_CHARTS_LETTERBOXD_URL) -> BeautifulSoup:
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

def extract_top_letterboxd_films(film_soup: BeautifulSoup) -> list[dict]:
    try:
        film_list = film_soup.find("ul", 
                                   {"class": "js-list-entries poster-list -p125 -grid film-list"})
        films = film_list.find_all('li', 
                                   {"class": "poster-container numbered-list-item"})
        clean_films = []
        for film in films:            
            film_info = {}
            film_info["film_name"] = film.find_all("img")[0].get('alt')
            film_info["film_rank"] = int(film.find("p", {"class" : "list-number"}).contents[0])
            film_info["letterboxd_link"] = "https://letterboxd.com" + film.find("div").get("data-target-link")
            clean_films.append(film_info)
        return clean_films
    except:
        print("Whoops")
        return None



if __name__ == "__main__":
    main_soup = load_top_letterboxd_soup(1)
    extract_top_letterboxd_films(main_soup)
    # with open("letterboxd_html_test.html", "w") as file:
    #     file.write(str(main_soup))
    # print(main_soup.find('ul', {"class": "js-list-entries poster-list -p125 -grid film-list"}))
