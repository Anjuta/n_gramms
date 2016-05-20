#!/usr/bin/python
from __future__ import division
import sys


def main():
    stat = dict()

    for line in sys.stdin:
        key, value = line.rsplit(' ', 1)
        key = tuple(key.split())
        stat[key] = int(value)

    for key, value in stat.items():
        if len(key) < 3:
            continue

        two_gramm = stat[(key[0], key[1])]
        print '({first_word}, {second_word}, {third_word}, {three_gramm}, {two_gramm}, {probability})'.format(
            first_word=key[0],
            second_word=key[1],
            third_word=key[2],
            three_gramm=value,
            two_gramm=two_gramm,
            probability=value/two_gramm,
        )


if __name__ == '__main__':
    main()
