#!/usr/bin/env python3

"""Script to clear file of written roman number."""

import sys
import os
import glob
import re
import ntpath
import num2words as n2w

DIR = 'clear_txt'

NUMERAL_MAP = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))


def roman_to_int(n):
    """Transform a roman number string into corresponding int."""
    i = result = 0
    for integer, numeral in NUMERAL_MAP:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result


def replace_in_file(path):
    """Copy the file passed in paramter with roman numbers spell in french.

    For .I. the program ask user to choose between 'un' or 'une'.
    """
    filename = ntpath.basename(path)
    print(filename)
    lines = []
    with open(path, 'r') as fd:
        lines = fd.readlines()
        fd.close()
    for j, line in enumerate(lines):
        words = line.split()
        for i, word in enumerate(words):
            match = re.match(r'\.([MCDXLIV]+)\.', word.upper())
            if match:
                if str(match.group()) == '.I.':
                    choice = '0'
                    while (choice != '1' and choice != '2'):
                        print(path, 'line:', j, '\n', ' '.join(words))
                        choice = input('Choose 1:un or 2:une\n')
                    if choice == '1':
                        word = 'un'
                    else:
                        word = 'une'
                else:
                    word = n2w.num2words(
                        roman_to_int(match.group(1)), lang='fr')
            words[i] = word
        lines[j] = ' '.join(words)
    text = '\n'.join(lines)
    path = os.path.join(DIR, filename)
    with open(path, 'w+') as fd:
        fd.write(text)
        print('{} have been created.'.format(path))


def main():
    """Convert files or print usage."""
    os.makedirs(DIR, exist_ok=os.path.exists(DIR))
    if len(sys.argv) > 1:
        argv = sys.argv[1:]
        for f in argv:
            replace_in_file(f)
    else:
        print('usage: ./clear_numbers.py FILENAME [FILENAME [...]]')


if __name__ == '__main__':
    main()
