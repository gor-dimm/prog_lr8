# Вариант 6
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def repl(param1, param2):
    def change(str):
        print(str)
        res = re.sub('[' + param1 + ']+', param2, str)
        return res
    return change


if __name__ == '__main__':
    print(repl("yi", "x")("yyysdiiiwqd"))
