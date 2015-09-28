#! /usr/bin/env python
__author__ = 'Johan'

import shutil

def copyFile(src, dest):
    try:
        shutil.copy('c/temp/a.txt', 'c/temp/moon/b.txt')
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)