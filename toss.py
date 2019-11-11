N = range(1,7)

#for i in N:
#    print(i)

#for i in N :
#    for j in N :
#	print (i+j)


S=list()
for i in N:
    for j in N:
        print(i,j)
        S.append(i+j)

G={}
for i in range(1,13):
    G[i]=0

for i in S :
    G[i]=G[i]+1

for i in S:
    if i in G:
        G[i] += 1
        G[i] = G[i] + 1
    else:
        G[i] = 0
        


print(G)
    
	
    
