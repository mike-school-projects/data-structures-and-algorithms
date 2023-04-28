import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    assert Hashtable

# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    # Changed order of results to fit my hash
    expected = [['ahmad', 30], ['listen', 'to me'], ['silent', True]]

    assert actual == expected

def test_duplicate_key():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("ahmad", True)

    actual = hashtable.get("ahmad")
    expected = True

    assert actual == expected

def test_integer_key():
    hashtable = Hashtable(1024)
    hashtable.set(5, 30)

    actual = hashtable.get(5)
    expected = 30

    assert actual == expected

def test_None_key():
    hashtable = Hashtable(1024)
    hashtable.set(None, 30)

    actual = hashtable.get(None)
    expected = 30

    assert actual == expected

def test_invalid_key():
    hashtable = Hashtable(1024)

    actual = hashtable.get('ahmad')
    expected = None

    assert actual == expected
