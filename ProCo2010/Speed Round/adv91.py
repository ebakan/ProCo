'''
Created on May 15, 2010

@author: ebakan
'''
import sys
if __name__ == '__main__':
    inp=sys.stdin.read().split('\n')
    key=inp[0]
    encrypted=inp[1]
    out=""
    for i in xrange(len(encrypted)):
        n=chr((ord(encrypted[i])-ord(key[i])+26)%26+65)
        out+=n
        if len(key)<len(encrypted):
            key+=n
    sys.stdout.write(out+'\n')