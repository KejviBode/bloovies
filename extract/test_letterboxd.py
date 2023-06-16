import pytest
from bs4 import BeautifulSoup
from letterboxd import extract_top_letterboxd_films

@pytest.fixture
def top_letterboxd_soup():
    with open("letterboxed_html_test.html", 'r', encoding='utf-8') as page:
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
    return soup

def test_top_letterboxd_invalid():
    assert extract_top_letterboxd_films(13456) is None

def test_top_letterboxd_soup_valid():
    test_soup = top_letterboxd_soup()
    assert extract_top_letterboxd_films(test_soup)
