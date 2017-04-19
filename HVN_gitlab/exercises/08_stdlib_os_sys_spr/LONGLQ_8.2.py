import sys
import inspect


def count_classes_function(fi):
    cls = []
    funcs = []
    module = __import__(fi)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            cls.append(name)
        if inspect.isfunction(obj):
            funcs.append(name)
    return cls, funcs


if __name__ == '__main__':
    try:
        cls, funcs = count_classes_function(sys.argv[1])
        print 'Classes:{0}\nNumber of Classes:{1}'.format(cls, len(cls))
        print 'Functions:{0}\nNumber of functions:{1}'.format(funcs, len(funcs))
    except IndexError:
        print 'Need a python code path'
