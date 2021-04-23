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
    required_charsets = set()
    if numbers:
        warn('using numbers in random password is recommended')
        required_charsets.add(NUMBERS)
    
    if special:
        warn('using special characters in random password is recommended')
        required_charsets.add(SPECIAL)
    
    if uppercase:
        warn('using uppercase letters in random password is recommended')
        required_charsets.add(UPPER)
    
    if lowercase:
        warn('using lowercase letters in random password is recommended')
        required_charsets.add(LOWER)

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