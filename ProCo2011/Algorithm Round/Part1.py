
def contains(table,char):
    for i in range(3):
	for j in range(3):
	    if(table[i][j].count(char)>0):
		return i
    return -1


if(__name__=='__main__'):
    table=[[['A','B','C'],['J','K','L'],['S','T','U']],
       [['D','E','F'],['M','N','O'],['V','W','X']],
       [['G','H','I'],['P','Q','R'],['Y','Z','']]]
    s1="STGDEYEEMYTLPVYUSLKZEURGJMZSLATRWPBYDDZVDEKRCIIGFWGFODQQYNJTWJOCTPIOGPGKQFTKHFRJRWNVQCLRPZZRCFXIUPPZNYQQHWAYIAHGWQBISLYMPZYLHKETFFXMUIXOSNVNNAAPFKW"
    s2="LZWYSFVCMZYPAIKXTVLCGXXINONNTJPHHAWQVTOYALPYZIDYFLEPXNTQPGBGPWYVCWTHCQZQCKUMNVRHGHSZNEVQFJSZPAYDRQRQKZNNDJIFNCEYBKEKMZDGIGIVVD"
    s3="KTIAAJKOQSSZUHYSVRJLTCGFMAERIHVWWHQGALOYRBQRGJPTSHGWNTOXCIJGNOMHKCIQQLGNZTWOCXHYHFENSGPVVLKCOEKMQEZLQSHIPMEQMEXEKDHHIBQDHJDPWRDWQKPQPUKYKVHZZTGEPKERCZYERJYEQPBRRHAPDMZVNWZ"
    s1l=[s1[i:i+3] for i in range(0,len(s1),3)]
    s2l=[s2[i:i+3] for i in range(0,len(s2),3)]
    s3l=[s3[i:i+3] for i in range(0,len(s3),3)]
    #s1
    s1o=[]
    for i in s1l:
	i1=contains(table,i[0])
	i2=contains(table,i[1])
	i3=contains(table,i[2])
	s1o.append(table[i1][i2][i3])
    s2o=[]
    for i in s2l:
	i1=contains(table,i[0])
	i2=contains(table,i[1])
	i3=contains(table,i[2])
	s2o.append(table[i1][i2][i3])
    s3o=[]
    for i in s3l:
	i1=contains(table,i[0])
	i2=contains(table,i[1])
	i3=contains(table,i[2])
	s3o.append(table[i1][i2][i3])

    print ''.join(s1o)
    print ''.join(s2o)
    print ''.join(s3o)
