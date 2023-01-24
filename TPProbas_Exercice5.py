import random
import math
import numpy as np
import matplotlib.pyplot as plt


def UniformeContinue(a,b):
    if a>b:
        return("Erreur il faut a<b")
    return a+(b-a)*random.random()


def BoxMuller(n):
    Xc=np.linspace(-10,10,n)
    Yc=np.zeros(n)

    for k in range(n):
        U=UniformeContinue(0,1)
        V=UniformeContinue(0,1)
        X=np.sqrt(-2*np.log(U))*np.cos(2*(np.pi)*V)
        Y=np.sqrt(-2*np.log(U))*np.sin(2*(np.pi)*V)
        for i in range(n-1):
            if(Xc[i]<=Y<Xc[i+1]):
                Yc[i]+=1
                
        
    plt.figure()
    plt.bar(Xc,Yc)
    plt.show()
        
BoxMuller(100)




