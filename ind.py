#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Вариант 6

def zamena(a, b):
    def change(str):
        str = str.replace(a, b)
        ans = ""
        for i in range(0, len(str)):
            if str[i] != str[i - 1]:
                ans += str[i]
        return ans
    return change


if __name__ == '__main__':
    print(zamena("y", "x")("yyysdyyyywqd"))
    print(zamena("I", "You")("I love NCFU!"))
