#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : commandlineArgs.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 14.07.2020
# Last Modified Date: 14.07.2020
# Last Modified By  : Joe Biggins <jjbiggins@joebiggins.io>

import os, sys

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][1] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]

    return opts

if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)



