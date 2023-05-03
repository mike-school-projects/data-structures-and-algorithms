import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = "[['diligent', ['employed', 'idle']], ['fond', ['enamored', 'averse']], ['guide', ['usher', 'follow']], ['outfit', ['garb', None]], ['wrath', ['anger', 'delight']]]"


    actual = str(left_join(synonyms, antonyms))

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_empty_right():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
    }

    expected = "[['diligent', ['employed', None]], ['fond', ['enamored', None]], ['guide', ['usher', None]], ['outfit', ['garb', None]], ['wrath', ['anger', None]]]"


    actual = str(left_join(synonyms, antonyms))

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_empty_left():
    synonyms = {
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = "[]"

    actual = str(left_join(synonyms, antonyms))

    assert actual == expected

