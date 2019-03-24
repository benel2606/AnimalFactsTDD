"""
unit testing for the 2 features:
1. searching by a word or string
2. searching by a date of creation.
"""
from __future__ import print_function
# from unittest.mock import Mock, patch
from mock import Mock, patch
from nose.tools import assert_equal  # pylint: disable=import-error
from animal_facts_function import get_animal_facts, get_facts_by_word
from animal_facts_mock_dictionary import facts


# Facts by word tests

@patch('requests.get')
def test_getting_facts_by_word_when_word_is_not_valid(mock_get):
    """
    passes if 0 is returned when searching an empty word, else fails
    :param mock_get:
    :return:
    """
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = facts
    response = get_animal_facts()
    assert_equal(len(get_facts_by_word(response.json(), "hsdghgd")), 0)
    print(get_facts_by_word(response.json(), "hxgfhdsgfh"))


@patch('requests.get')
def test_getting_facts_by_word_when_word_is_valid(mock_get):
    """
    passes if 2 facts are returned when searching 'years', else fails
    :param mock_get:
    :return:
    """
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = facts
    response = get_animal_facts()
    assert_equal(len(get_facts_by_word(response.json(), "years")), 2)
    print(len(get_facts_by_word(response.json(), "years")))


@patch('requests.get')
def test_getting_facts_by_word_when_word_is_not_string(mock_get):
    """
    passes if 0 facts are returned when searching with an argument
    that is not of type string, else fails
    :param mock_get:
    :return:
    """
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = facts
    response = get_animal_facts()
    assert_equal(len(get_facts_by_word(response.json(), 6)), 0)
    # print(len(get_facts_by_word(response.json(), 6)))


@patch('requests.get')
def test_getting_facts_by_word_when_no_argument_is_given(mock_get):
    """
    passes if 0 facts are returned when no arguments are given, else fails
    :param mock_get:
    :return:
    """
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = facts
    response = get_animal_facts()
    assert_equal(len(get_facts_by_word(response.json())), 0)
    # print(len(get_facts_by_word(response.json())))


@patch('requests.get')
def test_getting_facts_by_word_when_blank_word_is_given(mock_get):
    """
    passes if the 0 is return when searching an empty word e.g '   ', else fails
    :param mock_get:
    :return:
    """
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = facts
    response = get_animal_facts()
    assert_equal(len(get_facts_by_word(response.json(), "")), 0)
    # print(len(get_facts_by_word(response.json())))
