import sys


def head(file):
    with open(file, 'r') as f:
        count = 1
        lines = []
        for line in f:
            lines.append(line)
            count += 1
            if count > 10:
                break
    f.closed
    return lines


def tail(file):
    with open(file, 'r') as f:
        count = 0
        lines = []
        read_data = f.readlines()
        for line in read_data[-10:]:
            lines.append(line)
    f.closed
    return lines


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            for i in head(sys.argv[2]):
                print i
        elif sys.argv[1] == '-t':
            for i in tail(sys.argv[2]):
                print i
        else:
            print 'head or tail??'
            exit()
    except IndexError:
        print 'Need a file path'
