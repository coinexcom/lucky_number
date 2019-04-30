#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import random


def main(seeds, start_num, end_num, count):
    results = set()
    random.seed(int(seeds, 16))
    while len(results) < count:
        r = random.randint(start_num, end_num)
        results.add(r)

    for item in sorted(results):
        print item


if __name__ == '__main__':
    """
    python lucky_number.py "0000000000000000000b99fea8fac0fac12f045a95a07736f639a51dd70c47ff" 1000 10000 10
    """
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
