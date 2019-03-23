"""
tests
"""
import requests
from nose.tools import assert_true  # pylint: disable=import-error


def test_get_animal_facts():
    """
    :return:
    """
    url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat,dog,snail,horse&amount=500'
    response = requests.get(url)
    assert_true(response.ok)
    print(response.json()[0]["text"])
    if response.ok:
        return response

    return None
