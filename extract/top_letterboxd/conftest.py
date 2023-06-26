'''
Pytest fixtures used for test_letterboxd
'''
import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def top_letterboxd_soup():
    with open("letterboxd_html_test.html", 'r', encoding='utf-8') as page:
        html_bytes = page.read()
        soup = BeautifulSoup(html_bytes, "html.parser")
    return soup
