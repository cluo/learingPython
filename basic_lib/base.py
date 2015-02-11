#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-10
__author__ = 'cluo'

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


if __name__ == '__main__':
    pass
