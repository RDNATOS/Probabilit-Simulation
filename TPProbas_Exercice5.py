import random
import math
import numpy as np
import matplotlib.pyplot as plt


def UniformeContinue(a,b):
    if a>b:
        return("Erreur il faut a<b")
    return a+(b-a)*random.random()


def BoxMuller1(n):
    Xc=np.linspace(-10,10,n)
    Yc=np.zeros(n)

    for k in range(n):
        U=UniformeContinue(0,1)
        V=UniformeContinue(0,1)
        X=np.sqrt(-2*np.log(U))*np.cos(2*(np.pi)*V)
        Y=np.sqrt(-2*np.log(U))*np.sin(2*(np.pi)*V)
        for i in range(n-1):
            if(Xc[i]<=Y<Xc[i+1]):
                Yc[i]+=1/n
    
    
        
    plt.figure()
    plt.bar(Xc,Yc)
    plt.show()
    
def BoxMuller2(n,j):    ##n le nombre de val aléatoire et j le nombre d'intervalle de la représentation
    Xc=np.linspace(-10,10,j)
    Yc=np.zeros(j)
    W=[]

    for k in range(n):
        U=UniformeContinue(0,1)
        V=UniformeContinue(0,1)
        X=np.sqrt(-2*np.log(U))*np.cos(2*(np.pi)*V)
        Y=np.sqrt(-2*np.log(U))*np.sin(2*(np.pi)*V)
        W.append(Y)
        for i in range(j-1):
            if(Xc[i]<=Y<Xc[i+1]):
                Yc[i]+=1/n
    
    E=0
    V=0
    for k in range(j):
        E+=Xc[k]*Yc[k]
    for k in range(n):
        V+=((W[k]-E)**2)/n   
    
    print(f"On trouve une espérance expérimentale de {E}") 
    print(f"On trouve une Variance expérimentale de {V}")    
        
    plt.figure()
    plt.bar(Xc,Yc)
    plt.show()

        
#BoxMuller1(1000)
BoxMuller2(1000,500)





