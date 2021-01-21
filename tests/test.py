import pytest
import scraping.scraping as scraping

def test_scraping():
    df = scraping.collect_information('action', 100)
    assert df.shape == (100, 8)


def test_scraping_all():
    genres = ['action', 'comedy', 'sci-fi', 'horror']
    number_of_movies = 100
    df = scraping.collect_keywords(genres, number_of_movies)
    assert df.shape == (400, 8)