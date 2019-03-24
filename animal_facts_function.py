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


def get_facts_by_word(facts_dicts, filter_word=None):
    """
    This function gets a array of dictionaries of facts and a filter word
    and returns all the facts which contains the filter word.
    :param facts_dicts: Array of dicts, all the facts and their details.
    :param filter_word: String, the word to filter by.
    :return: Array of strings, all the facts which pass the filter.
    """
    result = []
    if filter_word is None or not isinstance(filter_word, str) or filter_word == "":
        return result

    facts_num = 0
    for fact in facts_dicts:
        if filter_word in fact["text"]:
            result.append(fact)
            facts_num += 1
            print("#" + str(facts_num) + " this fact is about " + fact["type"] + ":")
            print(fact["text"])
            print()

    return result


def get_facts_by_date(facts_dicts, filter_date=None):
    """
    This function gets a array of dictionaries of facts and a filter date
    and returns all the facts which were created at the given date.
    :param facts_dicts: Array of dicts, all the facts and their details.
    :param filter_date: String, the date of creation.
    :return: Array of strings, all the facts which pass the filter.
    """
    result = []
    if filter_date is None or not isinstance(filter_date, str) or filter_date == "":
        return result

    fd_split = str.split(filter_date, '-')
    if len(fd_split[0]) != 4 or len(fd_split[1]) != 2 or len(fd_split[2]) != 2:
        return result

    facts_num = 0
    for fact in facts_dicts:
        if "createdAt" in fact:
            date = fact["createdAt"][:10]
            if filter_date == date:
                result.append(fact)
                facts_num += 1
                print("#" + str(facts_num) + " this fact is about " + fact["type"] + ":")
                print(fact["text"])
                print()

    return result


FACTS = get_animal_facts().json()

def main_screen():
    """
    Simple Implementation for our features
    :return:
    """
    print("Welcome to Animal Facts App!")
    print("Press 1 to search facts by a word")
    print("Press 2 to search facts by a date")
    choice1 = input("your choice: ")
    while choice1 not in ('1', '2'):
        choice1 = input("invalid choice, choose again:")
    if choice1 == '1':
        print("Enter a word to search by: ")
        word = input()
        get_facts_by_word(FACTS, word)
        print("Would you like to search again or quit?")
        print("Press 1 to search again and 2 to quit")
        choice2 = input()
        while choice2 not in ('1', '2'):
            choice2 = input("invalid choice, choose again:")
        if choice2 == '1':
            main_screen()
        elif choice2 == '2':
            quit()

    elif choice1 == '2':
        print("Enter the date to search by")
        print("date must be in the format: yyyy-mm-dd")
        date = input()
        get_facts_by_date(FACTS, date)
        print("Would you like to search again or quit?")
        print("Press 1 to search again and 2 to quit")
        choice2 = input()
        while choice2 not in ('1', '2'):
            choice2 = input("invalid choice, choose again:")
        if choice2 == '1':
            main_screen()
        elif choice2 == '2':
            quit()

# main_screen()
