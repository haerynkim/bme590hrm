import pytest
from dictionary import add_to_dictionary

goodgoods = {'Burger': 8.7,
             'Ramen': 5.8
}

def test_add_to_dictionary():
    dictionary = add_to_dictionary(goodgoods, 'Sushi', 9.0)
    assert goodgoods['Sushi'] == 9.0

def test_excetion():
    with pytest.raises(TypeError):
        add_to_dictionary(goodgoods, 9.8, 5.5)