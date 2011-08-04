import sys
def gencodes(num):
    if(num==1):
	return ['0','1']
    else:
	tmp=gencodes(num-1)
	rev=[i for i in tmp]
	rev.reverse()
	tmp=['0'+i for i in tmp]
	rev=['1'+i for i in rev]
	return tmp+rev

if __name__=='__main__':
    bits=int(raw_input())
    inp=raw_input()
    codes=gencodes(bits)
    val=codes.index(inp)
    sys.stdout.write((bin(val)[2:]).zfill(bits))
    sys.stdout.write("\n")
    sys.stdout.flush()
    
