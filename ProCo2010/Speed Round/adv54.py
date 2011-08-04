'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__=='__main__':
    inp=sys.stdin.read().split('\n')
    lst=range(1,int(inp[0])+1)
    for i in xrange(len(lst)-1):
        j=i
        while len(lst)>1:
            del lst[j]
            j=(j+int(inp[1])-1)%(len(lst))
        if lst[0]==int(inp[0]):
            sys.stdout.write(str(i+1)+'\n')
            break
        lst=range(1,int(inp[0])+1)