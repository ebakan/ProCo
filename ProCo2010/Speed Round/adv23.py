'''
Created on May 15, 2010

@author: ebakan
'''
import sys
def getsum(inp):
    n=str(inp)
    if len(n)==1:
        return inp
    s=0
    for i in xrange(len(n)):
        s+=getsum(int(n[i])**2)
    return s
if __name__ == '__main__':
    n=sys.stdin.read()
    try:
        if getsum(int(n))==1:
            sys.stdout.write("happy\n")
        else:
            sys.stdout.write("sad\n")
    except RuntimeError:
        sys.stdout.write("sad\n")