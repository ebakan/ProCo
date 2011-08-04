'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__=='__main__':
    inp=sys.stdin.read().split()[1]
    x=map(int, inp)
    n=[]
    for i in xrange(1,len(x)):
        if (x[i]<=x[0]):
            n.append(x.pop(i))
    n.append(x.pop(0))
    for i in x:
        n.append(x.pop())
    f=map(str,n)
    sys.stdout.write(''.join(f)+'\n')
    
    