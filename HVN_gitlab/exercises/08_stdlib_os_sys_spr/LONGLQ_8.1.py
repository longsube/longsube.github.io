import sys


def cat_simulate(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            print line


if __name__ == '__main__':
    try:
        cat_simulate(sys.argv[1])
    except IndexError:
        print 'Need a file path'
