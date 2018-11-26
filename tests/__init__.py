import sys, os, platform

def import_test():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == 'Windows':
        sys.path.append(dir_name.split('\\tests')[0])
    elif platform.system() == 'Linux':
        sys.path.append(dir_name.split('/tests')[0])
