import pytest
from .movies import sort_title, sort_year, clean_titles, titles

def test_exists(movies):
    assert sort_title(movies)
    assert sort_year(movies)
    assert clean_titles('string')
    assert titles(movies)

def test_clean_titles_a():
    actual = clean_titles('a Movie Title')
    expected = 'Movie Title'
    assert actual == expected

def test_clean_titles_cap_a():
    actual = clean_titles('A Movie Title')
    expected = 'Movie Title'
    assert actual == expected

def test_clean_titles_an():
    actual = clean_titles('An Movie Title')
    expected = 'Movie Title'
    assert actual == expected

def test_clean_titles_the():
    actual = clean_titles('the Movie Title')
    expected = 'Movie Title'
    assert actual == expected

def test_clean_titles_none():
    actual = clean_titles('Movie Title')
    expected = 'Movie Title'
    assert actual == expected

def test_clean_titles_Another():
    actual = clean_titles('Another Movie Title')
    expected = 'Another Movie Title'
    assert actual == expected

def test_sort_year(movies):
    actual = titles(sort_year(movies))
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento",
                 "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert actual == expected

def test_sort_title(movies):
    actual = titles(sort_title(movies))

    expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]
    assert actual == expected

def test_sort_year_empty(movies):
    actual = titles(sort_year([]))
    expected = []
    assert actual == expected

def test_sort_titles_empty(movies):
    actual = titles(sort_title([]))
    expected = []
    assert actual == expected

@pytest.fixture
def movies():
    movies = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,

            "genres": ["Adventure", "Comedy"],
        },
        {
            "title": "Valkyrie",
            "year": 2008,
            "genres": ["Drama", "History", "Thriller"],
        },
        {
            "title": "Ratatouille",
            "year": 2007,
            "genres": ["Animation", "Comedy", "Family"],
        },
        {
            "title": "City of God",
            "year": 2002,

            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Memento",
            "year": 2000,

            "genres": ["Mystery", "Thriller"],
        },
        {
            "title": "The Intouchables",
            "year": 2011,

            "genres": ["Biography", "Comedy", "Drama"],
        },
        {
            "title": "Stardust",
            "year": 2007,
            "genres": ["Adventure", "Family", "Fantasy"],
        },
    ]
    return movies

