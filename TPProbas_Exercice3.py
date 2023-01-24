import random
import math
import numpy as np
import matplotlib.pyplot as plt



def UniformeContinue(a,b):
    if a>b:
        return("Erreur il faut a<b")
    return a+(b-a)*random.random()




def Question1(N):
    Y=[]
    X=[]
    Z=[]
    m=0.5   ## E[Xn]=0.5 car c'est l'espérance d'une loi uniforme sur [0,1]
    for n in range(1,N+1):
        X.append(n)
        S=0
        for k in range(n):
            u=UniformeContinue(0,1)
            S+=u/n
        Y.append(S)
    for k in range(N):
        Z.append(m)
        
    plt.figure()
    plt.plot(X,Y)
    plt.plot(X,Z)
    plt.show()
        
#Question1(1000)     

def G(p,l):
    return -((1/l)*np.log(1-p))

def expo(l):
    return G(random.random(),l)



def Question2(N,l):
    Y=[]
    X=[]
    Z=[]
    m=1/l   ## E[Xn]=1/l car c'est l'espérance d'une loi expo de paramètre l
    for n in range(1,N+1):
        X.append(n)
        S=0
        for k in range(n):
            u=expo(l)
            S+=u/n
        Y.append(S)
    for k in range(N):
        Z.append(m)
        
    plt.figure()
    plt.plot(X,Y)
    plt.plot(X,Z)
    plt.show()
        
#Question2(1000,0.5)  




def fInverse(p):
    return np.sqrt(p)

def f():
    return fInverse(random.random())



def Question3(N):
    Y=[]
    X=[]
    Z=[]
    m=2/3   ## E[Xn]=2/3 par calcul
    for n in range(1,N+1):
        X.append(n)
        S=0
        for k in range(n):
            u=f()
            S+=u/n
        Y.append(S)
    for k in range(N):
        Z.append(m)
        
    plt.figure()
    plt.plot(X,Y)
    plt.plot(X,Z)
    plt.show()
        
Question3(1000)  
















