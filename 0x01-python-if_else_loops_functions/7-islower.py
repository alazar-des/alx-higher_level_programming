#!/usr/bin/python3
def islower(c):
    '''
    Check if input is lower case.
    '''
    if (ord(c) >= ord('a')) and (ord(c) <= ord('z')):
        return True
    else:
        return False
