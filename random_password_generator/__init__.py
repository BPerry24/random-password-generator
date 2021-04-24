"""random password generation module"""
import random
import secrets
import string
import logging


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL = string.punctuation

logger = logging.getLogger('random_password_generator')

def generate_random_password(
    length:int=8,
    numbers:bool=True,
    special:bool=True,
    uppercase:bool=True,
    lowercase:bool=True
) -> str:
    """generates a cryptographically random and secure password
    """
    triples = [
        ('numbers', numbers, NUMBERS),
        ('special characters', special, SPECIAL),
        ('uppercase', uppercase, UPPER),
        ('lowercase', lowercase, LOWER)
    ]
    required_charsets = set()
    for name, boolean, chars in triples:
        if boolean:
            required_charsets.add(chars)
        else:
            warn(f'using {name} in random password is recommended')

    if not len(required_charsets):
        raise ValueError('options will result in empty password')

    password = ''
    for charset in required_charsets:
        password += secrets.choice(charset)
    
    
    all_chars = ''.join(required_charsets)
    if length not in range(8, 26):
        raise ValueError('`length` must be betweent 8 and 25')
    
    _length = secrets.choice(range(length, 26)) - len(password)
    password += ''.join((secrets.choice(all_chars) for _ in range(_length)))
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def warn(msg, *args):
    logger.warning(msg, *args)