def rot1(c,n):
    n=n%26
    val=ord(c)-65
    val-=n
    val=(val+26)%26
    return chr(val+65)

def rot2(c,n):
    n=n%26
    val=ord(c)-65
    val+=n
    val=(val+26)%26
    return chr(val+65)

"""
s1="SZWMFRGGAVYXJWUWSVVIJMZINQFOXCFEABZBZMJMDIQZGCFL"
s2="BGXJWUMWLDMLFTMLPWVMUTMJWXEGZVAAVLPWXJMNQGCKAWVLMFKW"
s3="BZMOQVBZBGCKMXWJBZMLPAZVTWOAALPWVMUTMJWXNSKLWJAGNP"
"""
s1="EW PGXW GGC SZW MFRGGAVY XJWUW SVV IJM ZINQFO XCF EABZ BZM JMDIQ ZGCFL"
s2="BG XJWUMWL DML F TM LPW VMUTMJ WX EGZVA AV LPW XJMNQGCK AWVLMFKW"
s3="BZM OQVBZ BG CKM XWJ BZM LPAZV TWO AA LPW VMUTMJ WX NSKLWJA GN P"
o1=[]
o2=[]
o3=[]

"""
o1=[rot1(s1[i],528)+rot2(s1[i+1],528) if i!=' 'else ' 'for i in range(0,len(s1),2)]
o2=[rot1(s2[i],528)+rot2(s2[i+1],528) if i!=' 'else ' 'for i in range(0,len(s2),2)]
o3=[rot1(s3[i],528)+rot2(s3[i+1],528) if i!=' 'else ' 'for i in range(0,len(s3),2)]

"""

tf=True
for i in s1:
    if(i==' '):
	o1.append(' ')
	continue
    if(tf):
	o1.append(rot1(i,528))
	tf=not tf
    else:
	o1.append(rot2(i,528))
	tf=not tf
tf=True
for i in s2:
    if(i==' '):
	o2.append(' ')
	continue
    if(tf):
	o2.append(rot1(i,528))
	tf=not tf
    else:
	o2.append(rot2(i,528))
	tf=not tf
tf=True
for i in s3:
    if(i==' '):
	o3.append(' ')
	continue
    if(tf):
	o3.append(rot1(i,528))
	tf=not tf
    else:
	o3.append(rot2(i,528))
	tf=not tf
    

print ''.join(o1)
print ''.join(o2)
print ''.join(o3)

a="LJDDLKHKHTSIDZHP"
ab=[rot1(a[i],3)+rot2(a[i+1],3) if i!=' 'else ' 'for i in range(0,len(a),2)]
print ''.join(ab)

