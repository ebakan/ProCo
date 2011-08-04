'''
Created on May 15, 2010

@author: ebakan
'''
import sys
def ispal(inp):
    reversed=inp[::-1]
    return inp==reversed

def getsmallpal(inp):
    if ispal(inp):
        return inp
    else:
        return getsmallpal(inp[1:])
if __name__=='__main__':
    inp=sys.stdin.read()
    sys.stdout.write(str(2*len(inp)-len(getsmallpal(inp)))+'\n')