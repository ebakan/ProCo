'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__ == '__main__':
    inp=sys.stdin.read().split('\n')[1:]
    for i in range(len(inp)):
        inp[i]=map(int,inp[i].split())
    col1=[i[0] for i in inp]
    col2=[i[1] for i in inp]
    maxinit=max(col2)
    m=col2.index(maxinit)
    corresponding=col1[m]
    for i in xrange(col2.count(maxinit)):
        y=[]
        x=0
        for j in range(i):
            x=inp[x:].index(maxinit)
        
    