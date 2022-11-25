from random import *
from time import *
from math import *


def factor(N):
    p=[]
    for d in range(2,int(sqrt(N))+1):
        if N % d == 0:
            p.append(d)
            N=N//d
    if N>1:
        p.append(N)
    return p

r0=10000000000
r1=r0*10
N=3
while N>0:
    p=randint(r0,r1)
    timeBegin=time()
    L=factor(p)
    timeEnd=time()
    if len(L)==1:
        print (F"{p}, {timeEnd-timeBegin:.2f}, sec")
        N=N-1
