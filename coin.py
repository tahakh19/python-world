




import random

#random.randint(0.1)
def coin():
    return random.randint(0,1)

def toss():
    return random.randint(1,6)

#print(toss(),toss())
#print(coin(),coin())
N = int(input('enter a nomber:'))
h_counter = 0
t_counter = 0
for i in range(N):
   #print(coin())
    c = coin()
    if c==0:
        t_counter = t_counter + 1
    if c==1:
        h_counter = h_counter + 1
print(h_counter, t_counter, h_counter + t_counter)



