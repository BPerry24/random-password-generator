# Random Password Generator #
A cryptographically random and secure password generator which relies only on the standard python library

## Usage ##
```python
from random_password_generator import generate_random_password

# password with default options (at least one upper, lower, special, and number character. 8 ≤ length ≤ 25)
password = generate_random_password()

# password of specified minimum length. must be between 8 and 25
password = generate_random_password(length=15)

# password without special characters
password = generate_random_password(special=False)

# password without capital letters
password = generate_random_password(uppercase=False)

#password without lowercase letters
password = generate_random_password(lowercase=False)

# password without numbers
password = generate_random_password(numbers=False)
```