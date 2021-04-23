"""password generation script enables running this package as a module
   using the default arguments of the function

   TODO allow user to pass args
"""
from . import generate_random_password


if __name__ == '__main__':
    print(generate_random_password())