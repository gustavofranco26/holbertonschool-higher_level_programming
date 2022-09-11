#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    counter = len(sys.argv)
    if counter == 1:
        print('{:d} arguments.'.format(counter - 1))
    else:
        if counter == 2:
            print('{:d} argument:'.format(counter - 1))
        else:
            print('{:d} arguments:'.format(counter - 1))
        for av in range(1, counter):
            print('{:d}: {}'.format(av, (sys.argv[av])))
