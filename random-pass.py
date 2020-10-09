#! usr/bin/python
# -*- coding: ISO-8859-1 -*-

import sys
import random
import string


def CreatePassword(size, numbers, special_characters):

    password_length = size
    password = ''

    for i in range(0, password_length):
        password = password + random.choice(string.digits*numbers)
        numbers = numbers-1
        password = password + \
            random.choice(string.punctuation*special_characters)
        special_characters = special_characters-1
        password = password + random.choice(string.letters)

    return(password)


def main():
    try:
        print(CreatePassword(int(sys.argv[1]), int(
            sys.argv[2]), int(sys.argv[3])))

    except (ValueError, IndexError):
        print('\033[93m%s\x1b[0m' % "Ooops.. Please try : \n"
              "python random-pass.py 'Size of your password' 'Number wanted' 'Special characters wanted'")


if __name__ == "__main__":
    main()
