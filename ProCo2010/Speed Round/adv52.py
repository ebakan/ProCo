'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__ == '__main__':
    inp=sys.stdin.read().split('\n')
    out1=[]
    out2=[]
    for i in inp[1]:
        try:
            inp[0].index(i)
        except ValueError:
            out1+=i
    for i in inp[0]:
        try:
            inp[1].index(i)
        except ValueError:
            out2+=i
    o1=''.join(out1)+'\n'
    if len(o1)==1:
        o1="none\n"
    o2=''.join(out2)+'\n'
    if len(o2)==1:
        o2="none\n"
    sys.stdout.write(o1)
    sys.stdout.write(o2)