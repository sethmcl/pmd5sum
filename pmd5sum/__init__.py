# coding=utf-8

import hashlib
import sys

def md5(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()


def print_usage():
    bin = sys.argv[0].split('/')[-1].split('.')[0]
    print 'Usage: %s [file path]' % bin

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    else:
        print md5(sys.argv[1])
