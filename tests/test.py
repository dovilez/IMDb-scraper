import pytest
import requests
from bs4 import BeautifulSoup
from scraping import scraping
import os
import pandas as pd


def test_exists():
    assert os.path.isfile("./scraping/scraping.py")


def test_data_exists():
    assert os.path.isfile("./tests/test_data/test_data.html")


def test_scraping():
    df = scraping.collect_information("action", 100)
    assert df.shape == (100, 8)


def test_scraping_one_page():
    with open("tests/test_data/test_data.html", encoding="utf8") as page:
        soup = BeautifulSoup(page, "html.parser")
    df = scraping.collect_page_information(soup)
    assert df.shape == (50, 8)


def test_scraping_all():
    genres = ["action", "comedy", "sci-fi", "horror"]
    number_of_movies = 100
    df = scraping.collect_keywords(genres, number_of_movies)
    assert df.shape == (400, 8)


def test_preprocess():
    data_wrong = {
        "year": ["(2021– )", "(2019–2020)"],
        "duration": ["43 min", "104 min "],
        "genre": [",Action, Drama, History", ",Action"],
    }
    df_wrong = pd.DataFrame(data=data_wrong)

    data_correct = {
        "year": ["2021", "2019"],
        "duration": ["43", "104"],
        "genre": [["Action", "Drama", "History"], ["Action"]],
    }
    df_correct = pd.DataFrame(data=data_correct)
    df_preprocessed = scraping.process_data(df_wrong)

    assert df_preprocessed.equals(df_correct) == True
