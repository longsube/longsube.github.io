import sys
import inspect
import collections
import os

def module_class_function(fle):
    module = __import__(fle)
    mdl = None
    cls = None
    func = None
    if inspect.ismodule(module):
        mdl = fi
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                cls = name
            if inspect.isfunction(obj):
                func = name
    return mdl, cls, func   


def variable(fle):
    module = __import__(fle)
    vbles = []
    if inspect.ismodule(module):
        with open(module) as f:
            for line in f:
                if '=' in line:
                    vbles.append(line.rstrip().split('=')[0])
    return vbles


def main(pkg):
    mdls = []
    clss = []
    funcs = []
    p_vbles = []
    for root, dirs, files in os.walk(pkg, topdown=False):
        for name in files:
            mdl, cls, func = module_class_function(os.path.join(root, name))
            vbls = variable(os.path.join(root, name))
            if not vbls:
                p_vbles.append(vbls)
            if mdl is not None:
                mdls.append(mdl)
                if cls is not None:
                    clss.append(cls)
                if func is not None:
                    funcs.append(func)  
    li_vbles = [v for i in range(0,len(p_vbles)) for v in p_vbles[i]]
    most_used_variables = [v for v in collections.Counter(li_vbles).most_common(10)]
    print 'Modules:{0}\nNumber of modules:{1}'.format(mdls, len(mdls))
    print 'Classes:{0}\nNumber of Classes:{1}'.format(clss, len(clss))
    print 'Functions:{0}\nNumber of functions:{1}'.format(funcs, len(funcs))
    print 'Most used variables: '%(most_used_variables)


    if __name__ == '__main__':
        try:
            main(sys.argv[1])
        except IndexError:
            print 'Need a python code path'
       