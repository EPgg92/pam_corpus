#!/usr/bin/env python3

"""Script to transform a xml into a txt."""

import sys
from bs4 import BeautifulSoup

TAG_TO_REMOVE = ['note', 'sic', 'hi', 'speaker', 'head', 'stage']


def get_text():
    """Print cleaned verses of xml file passed in argv[1]."""
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 1 and len(argv[0]) > 4 and argv[0][-4:] == '.xml':
        with open(argv[0]) as stream:
            lines = stream.readlines()
            str0 = ''
            for line in lines:
                line = line.replace('\n', '')
                line = line.replace('<lb', '\n<lb')
                line = line.replace('<div', '\n<div')
                line = line.replace('<ab', '\n<ab')
                str0 += ' ' + line
            soup = BeautifulSoup(str0, "xml")
            for tag in TAG_TO_REMOVE:
                for rem in soup(tag):
                    rem.extract()
            print(soup.body.get_text())
    else:
        print("usage: ./xml_txt.py filename.xml")


if __name__ == '__main__':
    get_text()
