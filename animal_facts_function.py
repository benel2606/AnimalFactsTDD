"""
AnimalFacts features:
1. search by word or string.
2. search by date.
"""
import requests


def get_animal_facts():
    """
    This function first makes a request to the cat-fact api
    for 500 random facts of all the animal types: cat, dog, horse, snail
    and returns then
    :return: response - JSON, if the request is successful
             None, else
    """
    url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat,dog,snail,horse&amount=500'
    response = requests.get(url)
    return response


def get_facts_by_word(facts_dict, filter_word=None):
    """
    This function gets a array of dictionaries of facts and a filter word
    and returns all the facts which contains the filter word.
    :param facts_dict: Array of dicts, all the facts and their details.
    :param filter_word: String, the word to filter by.
    :return: Array of strings, all the facts which pass the filter.
    """
    result = []
    if filter_word is None or not isinstance(filter_word, str) or filter_word == "":
        return result

    facts_num = 0
    for fact in facts_dict:
        if filter_word in fact["text"]:
            result.append(fact)
            facts_num += 1
            print("#" + str(facts_num) + " this fact is about " + fact["type"] + ":")
            print(fact["text"])
            print()
    return result
