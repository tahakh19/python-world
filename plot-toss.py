import random as rand
import matplotlib.pyplot as plt
#import time
def toss ():
    return rand.randint(1,6)    
#x=toss()
#print(x)
N=int(input ('enter number:'))
#for i in range( N ):
#    print (i,toss())
x=range(N)
y=[toss()+toss() for _ in x]
d=dict()
#for i in range(1, 13):
#    d[i] = 0;
    
for s in y:
    if s in d:
        d[s] += 1
    else:
        d[s]=1

print(d)
print(d.keys())
print(d.values())

xx = sorted(d)
yy=[ d[i] for i in xx]

print(xx)
print(yy)

#y={ for i in x}
#plt.plot(list(d.keys()), list(d.values()))
plt.plot(xx, yy)

d={}
NN = 0
for i in range(1, 7):
    for j in range(1, 7):
        s = i+j
        #print (d)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
        #print(i, j, s, d), 
        NN += 1

print("NN=", NN)

xx = sorted(d)

pp={i:d[i]/NN for i in xx}
yy=[ pp[i]*N for i in xx]
print("pp=", pp)


#yy2 = [d[i] * N for i in xx]
plt.plot(xx, yy)
#plt.plot(xx, yy2)
        
plt.show()



    
