'''
This python script will scrape from letterboxd
'''
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime

TOP_CHARTS_LETTERBOXD_URL = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/"
BASE_LETTERBOXD_URL = "https://letterboxd.com"


def load_top_letterboxd_soup(letterboxd_url: str = TOP_CHARTS_LETTERBOXD_URL,
                             page_num: int = None) -> BeautifulSoup:
    '''
    Load BeautifulSoup from Letterboxd top 250 reviewed films of all time
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
        return {"error" : True,
                "code" : err.code,
                "message" : err}

def extract_top_letterboxd_films(film_soup: BeautifulSoup) -> list[dict]:
    '''
    Extracts a list of the top films for a specific letterboxd page
    '''
    try:
        film_list = film_soup.find("ul",
                                   {"class": "js-list-entries poster-list -p125 -grid film-list"})
        films = film_list.find_all('li',
                                   {"class": "poster-container numbered-list-item"})
        clean_films = []
        for film in films:
            film_info = {}
            film_info["film_name"] = film.find_all("img")[0].get('alt')
            # film_info["release_year"] = film.find("div")


            # # Should film rank be here? I think should be in another area of the script


            film_info["film_rank"] = int(film.find("p", {"class" : "list-number"}).contents[0])


            film_info["letterboxd_link"] = BASE_LETTERBOXD_URL + film.find("div").get("data-target-link")
            clean_films.append(film_info)
        return clean_films
    except:
        print("Whoops")
        return None


def extract_film_cast(cast_url: str) -> list:
    try:
        film_page = load_top_letterboxd_soup(cast_url)
        cast = film_page.find( "div", 
                            {"class": "cast-list text-sluglist"}).find_all("a")
        cast_list = []
        for member in cast:
            cast_list.append({"character": member.get("title"), 
                            "actor": member.contents[0]})
        year = film_page.find("small", {"class" : "number"}).find("a").contents[0]
        return cast_list, year
    except Exception as err:
        return err, "Unknown year"


def extract_film_crew(crew_url: str) -> dict:
    try:
        crew_page = load_top_letterboxd_soup(crew_url)
        crew = crew_page.find("div", {"id": "tab-crew"}).find_all("a")
        directors = [director.contents[0] for director in crew if 'director' in director.get("href")]
        writers = [writer.contents[0] for writer in crew if 'writer' in writer.get("href") and "original" not in writer.get("href")]
        composers = [composer.contents[0] for composer in crew if 'composer' in composer.get("href")]
        return {"directors" : directors, "writers" : writers, "composers" : composers}
    except Exception as err:
        return err
        

def extract_film_details(details_url: str) -> dict:
    try:
        details_page = load_top_letterboxd_soup(details_url)
        details = details_page.find("div", {"id": "tab-details"}).find_all("a")
        studios = [studio.contents[0] for studio in details if "studio" in studio.get("href")]
        country = [country.contents[0] for country in details if "country" in country.get("href")][0]
        language = [language.contents[0] for language in details if "language" in language.get("href")][0]
        return {"studios" : studios,
                "country" : country,
                "language" : language}
    except Exception as err:
        return err


def extract_film_genres(genres_url: str) -> list:
    try:
        genres_page = load_top_letterboxd_soup(genres_url)
        genres = genres_page.find("div", {"id" : "tab-genres"}).find_all("a")
        return [genre.contents[0] for genre in genres if "genre" in genre.get("href")]
    except Exception as err:
        return err


def extract_letterboxd_film_page(film : dict) -> dict:
    if "letterboxd_link" not in film.keys():
        film["error"] = "Invalid letterboxd film link"
        return film
    url = film["letterboxd_link"]
    crew_url = url + "crew"
    details_url = url + "details"
    genres_url = url + "genres"
    try:
        cast_list, release_year = extract_film_cast(url)
        if isinstance(cast_list,list):
            film["cast_list"] = cast_list
            film["release_year"] = release_year
        else:
            film["cast_error"] = cast_list
            film["release_year_error"] = release_year
        crew = extract_film_crew(crew_url)
        if isinstance(crew, dict):
            film["directors"] = crew["directors"]
            film["writers"] = crew["writers"]
            film["composers"] = crew["composers"]
        else:
            film["crew_error"] = crew
        details = extract_film_details(details_url)
        if isinstance(details, dict):
            film["studios"] = details["studios"]
            film["country"] = details["country"]
            film["language"] = details["language"]
        else:
            film["details_error"] = details
        genres = extract_film_genres(genres_url)
        if isinstance(genres, list):
            film["genres"] = genres
        else:
            film["genres_error"] = genres
        return film
    except HTTPError as err:
        film["http_error"] = err
        return film
    except Exception as err:
        film["error"] = err
        return film


def scrape_multiple_pages():
    all_films = []
    for i in range(1,4):
        letterboxd_soup = load_top_letterboxd_soup(TOP_CHARTS_LETTERBOXD_URL, i)
        films = extract_top_letterboxd_films(letterboxd_soup)
        for film in films:
            all_films.append(extract_letterboxd_film_page(film))
    return all_films



if __name__ == "__main__":
    START = datetime.now()
    print(f"Start time: {START}")
    filmage = scrape_multiple_pages()
    print(filmage)
    END = datetime.now()
    print(f"End time: {END}")
    duration = END - START
    print(f"Duration: {duration}")
