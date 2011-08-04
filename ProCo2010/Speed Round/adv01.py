'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__ == '__main__':
    ints = sys.stdin.readline().split()
    for i in range(len(ints)):
        ints[i]=int(ints[i])
    while ints[0]<=6 and ints[1]<=6 and ints[2]<=6:
        sys.stdout.write("R")
        ints[2]+=ints[0]
        if ints[2]>6:
            sys.stdout.write(" Win")
            break
        #sys.stdout.write('\r')
        #sys.stdout.flush()
        string = raw_input("test")
        if string=="R":
            ints[0]+=ints[2]
        else:
            ints[0]+=ints[1]
        if ints[0]>6:
            sys.stdout.write("Lose")
            break
        sys.stdout.flush()