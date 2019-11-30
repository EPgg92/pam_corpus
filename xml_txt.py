#!/usr/bin/env python3

"""Script to transform a xml into a txt."""

import argparse
from bs4 import BeautifulSoup

TAG_TO_REMOVE = ['note', 'sic', 'hi', 'speaker', 'head', 'stage']


def get_argparser():
    parser = argparse.ArgumentParser(
        description='Transform many xml into txt.')
    parser.add_argument('filenames', nargs='+', metavar='filename',
                        help='Path of file to transform.',
                        type=argparse.FileType('r'))
    args = parser.parse_args()
    return args


def get_text(argv):
    """Print cleaned verses of xml file passed in argv[1]."""
    if len(argv.name) > 4 and argv.name[-4:] == '.xml':
        lines = argv.readlines()
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
        text = soup.body.get_text()
        with open(argv.name[:-4] + '.txt', 'w+') as stream:
            stream.write(text)
            stream.close()
        print('{}.txt is created.'.format(argv.name[:-4]))
    else:
        print('{} is not an xml file.'.format(argv))


if __name__ == '__main__':
    ARGS = get_argparser()
    for FILE in ARGS.filenames:
        get_text(FILE)
