import sys
inp=sys.stdin.readline().split(' ')
numTokens=int(inp[0])
numLines=int(inp[1])
tokens=[]
for i in range(numTokens):
    tokens.append(sys.stdin.readline()[:-1])
inp=[]
for i in range(numLines):
    inp.append(sys.stdin.readline())
out=[]
for i in inp:
    tmp=i
    for j in range(len(tokens)):
        tmp=tmp.replace("<"+str(j+1)+">",tokens[j])
    out.append(tmp)
sys.stdout.write(''.join(out)+'\n')
sys.stdout.flush()
