'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__ == '__main__':
    inp = sys.stdin.read().split('\n')
    tf=True
    for i in xrange(1,int(inp[0])+1):
        inp[i]=map(int, inp[i].split())
    n=sum(inp[i])
    for i in xrange(1,len(inp[1])):
        s=0
        for j in xrange(1,len(inp[1])+1):
            s+=inp[j][i]
        if sum(inp[i])!=n or s!=n:
            tf=False
    if tf:
        sys.stdout.write("yes\n")
    else:
        sys.stdout.write("no\n")