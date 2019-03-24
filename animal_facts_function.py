import requests


def get_animal_facts():
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat,dog,snail,horse&amount=500')
    if response.ok:
        return response
    else:
        return None
