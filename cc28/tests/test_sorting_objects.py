import pytest

from cc28.sorting_objects import sort_by_recent_year, sort_strings

list = [
    {"title": "The aa", "year": 2018},
    {"title": "zz aa", "year": 2016},
    {"title": "dd", "year": 2020},
    {"title": "The bb", "year": 2016},
    {"title": "The cc", "year": 2010},
]

# Test for sort_by_year function
def test_sort_by_recent_year():
    sorted_movies = sort_by_recent_year(list)
    expected_result = [
        {"title": "dd", "year": 2020},
        {"title": "The aa", "year": 2018},
        {"title": "zz aa", "year": 2016},
        {"title": "The bb", "year": 2016},
        {"title": "The cc", "year": 2010},
    ]
    assert sorted_movies == expected_result
    print("sort_by_year test passed")

# Test for sort_by_title function
def test_sort_strings():
    sorted_movies = sort_strings(list)
    expected_result = [
    {"title": "The aa", "year": 2018},
    {"title": "The bb", "year": 2016},
    {"title": "The cc", "year": 2010},
    {"title": "dd", "year": 2020},
    {"title": "zz aa", "year": 2016},
    ]
    assert sorted_movies == expected_result
    print("sort_by_title test passed")