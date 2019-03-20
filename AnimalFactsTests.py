from nose.tools import *
import requests

def  test_get_animal_facts():
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat,dog,snail,horse&amount=500')
    assert_true(response.ok)
    if response.ok:
        return response
    else:
        return None
