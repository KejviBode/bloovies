'''
This python script will scrape from letterboxd the most popular films this week
'''
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime

from extract_functions import load_letterboxd_soup
from top_letterboxd.letterboxd import extract_letterboxd_film_page, extract_film_reviews

TOP_50_WEEKLY_URL = ""
WEEKLY_LETTERBOXD_URL = "https://letterboxd.com/films/ajax/popular/this/week/year/2023/page/1/"
BASE_LETTERBOXD_URL = "https://letterboxd.com"

def extract_weekly_films(letterboxd_soup: BeautifulSoup) -> list:
    film_ul = letterboxd_soup.find("ul",
                                {"class": "poster-list -p70 -grid"})
    films = film_ul.find_all("li", 
                             {"class": "listitem poster-container"})
    clean_films = []
    for film in films[:1]:
        clean_film = {}
        clean_film["film_name"] = film.find("img").get("alt")
        clean_film["letterboxd_link"] = BASE_LETTERBOXD_URL + film.find("div").get("data-film-slug")
        clean_films.append(clean_film)
        # print(film)
    print(clean_films)
    return clean_films


if __name__ == "__main__":
    print("Yyyyyello")
    soup = load_letterboxd_soup(WEEKLY_LETTERBOXD_URL)
    # with open("html_weekly_films_test.html", "w") as page:
    #     page.write(str(soup))
    main_films = extract_weekly_films(soup)
    main_film = extract_letterboxd_film_page(main_films[0])
    extract_film_reviews(
        main_film["letterboxd_link"] + "reviews/by/activity/page/1/")
    # print(main_film)