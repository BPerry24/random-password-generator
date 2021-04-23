"""random password generator test suite
"""

import string

import pytest

from random_password_generator import generate_random_password

UPPER_CASE = string.ascii_uppercase
LOWER_CASE = string.ascii_lowercase
SPECIAL = string.punctuation
NUMBERS = string.digits

def test_generate_random_password_defaults():
    """generates a random password between 8 and 15 chars long with
       special, upper, lower, and number chars
    """
    password = generate_random_password()
    assert len(password) in  range(8, 26)
    required_chars = {
        'upper': False,
        'lower': False,
        'special': False,
        'numbers': False
    }
    upper = set(UPPER_CASE)
    lower = set(LOWER_CASE)
    special = set(SPECIAL)
    numbers = set(NUMBERS)

    for char in password:
        if char in upper:
            required_chars['upper'] = True
        
        if char in lower:
            required_chars['lower'] = True
        
        if char in special:
            required_chars['special'] = True
        
        if char in numbers:
            required_chars['numbers'] = True
    
    for k, v in required_chars.items():
        assert v, f'missing {k}'


def test_generate_random_password_provide_length():
    """generates a random password with the minimum desired length
    """
    password = generate_random_password(length=20)
    assert len(password) >= 20

@pytest.mark.parametrize(('kwargs', 'charset'), (
    ({'special': False}, set(SPECIAL)),
    ({'numbers': False}, set(NUMBERS)),
    ({'uppercase': False}, set(UPPER_CASE)),
    ({'lowercase': False}, set(LOWER_CASE))
))
def test_generate_random_password_without_special_chars(kwargs, charset):
    """generates a random password without `string.punctuation`
    """
    password = generate_random_password(**kwargs)
    for char in password:
        assert char not in charset

@pytest.mark.parametrize(('length',), (
    (7,),
    (27,)
))
def test_generate_random_password_provided_length_not_in_bounds(length):
    """raise value error"""
    with pytest.raises(ValueError):
        generate_random_password(length=length)

def test_generate_random_password_all_disabled():
    """raise value error"""
    with pytest.raises(ValueError):
        generate_random_password(lowercase=False, uppercase=False, numbers=False, special=False)