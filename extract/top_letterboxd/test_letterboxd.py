'''
Tests for letterboxd scraping script
'''
import pytest
from letterboxd import extract_top_letterboxd_films
from conftest import top_letterboxd_soup


def test_top_letterboxd_invalid():
    assert extract_top_letterboxd_films(13456) is None

def test_top_letterboxd_soup_valid(top_letterboxd_soup):
    # test_soup = top_letterboxd_soup()
    html_films = extract_top_letterboxd_films(top_letterboxd_soup)
    assert html_films[0]["film_name"] == "Spider-Man: Across the Spider-Verse"
    assert html_films[0]["film_rank"] == 1
    assert html_films[0]["letterboxd_link"] == "https://letterboxd.com/film/spider-man-across-the-spider-verse/"
