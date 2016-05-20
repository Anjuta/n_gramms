#!/usr/bin/python
import sys


PUNCTUATION = ',./~`!@#$%^&()*_=+"\'?\n '


def get_three_gramms(sentence):
    res = []
    words = sentence.split(' ')

    for i in range(2, len(words)):
        first = words[i-2].strip(PUNCTUATION)
        second = words[i-1].strip(PUNCTUATION)
        third = words[i].strip(PUNCTUATION)

        if not first or not second or not third:
            continue

        res.append('{} {} {}'.format(first, second, third))

    return res


def get_two_gramms(sentence):
    res = []
    words = sentence.split(' ')

    for i in range(1, len(words)):
        first = words[i-1].strip(PUNCTUATION)
        second = words[i].strip(PUNCTUATION)

        if not first or not second:
            continue

        res.append('{} {}'.format(first, second))

    return res


def main():
    stat = dict()

    for line in sys.stdin:
        _, sentence = line.split('\t', 1)
        sentence = sentence.lower()

        n_gramms = get_two_gramms(sentence)
        n_gramms.extend(get_three_gramms(sentence))

        for e in n_gramms:
            val = stat.get(e, 0)
            stat[e] = val + 1

    for key, value in stat.items():
        print key, value


if __name__ == '__main__':
    main()
