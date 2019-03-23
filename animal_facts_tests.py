import requests
from nose.tools import assert_true # pylint: disable=import-error


def test_get_animal_facts():
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat,dog,snail,horse&amount=500')
    assert_true(response.ok)
    if response.ok:
        return response

    return None
