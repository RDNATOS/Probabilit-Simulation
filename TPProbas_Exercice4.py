import random
import math

import keyboard
import numpy as np
import matplotlib.pyplot as plt
import time



def UniformeContinue(a,b):
    if a>b:
        return "Erreur il faut a<b"
    return a+(b-a)*random.random()




# def Question1a(N):
#     Y=[]
#     X=[]
#     Z=[]
#     m=0.5   ## E[Xn]=0.5 car c'est l'espérance d'une loi uniforme sur [0,1]
#     sigma=1/12 
#     for n in range(1,N+1):
#         X.append(n)
#         S=0
#         for k in range(n):
#             u=UniformeContinue(0,1)
#             S+=u/n
#         Y.append(S)
#     for n in range(N):
#         Z.append((Y[n]-m)*(np.sqrt(n+1)/sigma))
    
    
    
#     plt.figure()
#     #plt.plot(X,Y)
#     plt.plot(X,Z)
#     plt.show()
        
#Question1a(1000)   

#####################################################################################

    
def Question1b(N,j):
    Y=[]
    X=[]
    Z=[]
    m=0.5   ## E[Xn]=0.5 car c'est l'espérance d'une loi uniforme sur [0,1]
    sigma=1/12 
    for n in range(1,N+1):
        X.append(n)
        S=0
        for k in range(n):
            u=UniformeContinue(0,1)
            S+=u/n
        Y.append(S)
    for n in range(N):
        Z.append((Y[n]-m)*(np.sqrt(n+1)/sigma))
    
    X=np.linspace(-20,20,j)
    W=np.zeros(j)
    for n in range(N):
        for k in range(j):
            if X[k]<=Z[n]<X[k+1]:
                W[k]+=1/N
    
    E=0
    V=0
    for k in range(N):
        E+=X[k]*W[k]
    print(f"On trouve une espérance expérimentale de {E}") 
    for k in range(N):
        V+=((Z[k]-E)**2)/N   
    print(f"On trouve une Variance expérimentale de {V}") 

                
    plt.figure()
    plt.bar(X,W)
    plt.show()    
    


#Question1b(1000,1000)

#####################################################################################






def G(p,l):
    return -((1/l)*np.log(1-p))

def expo(l):
    return G(random.random(),l)


# def Question2a(N,l):
#     Y=[]
#     X=[]
#     Z=[]
#     m=1/l
#     sigma=1/(l**2)
#     for n in range(1,N+1):
#         X.append(n)
#         S=0
#         for k in range(n):
#             u=expo(l)
#             S+=u/n
#         Y.append(S)
#     for n in range(N):
#         Z.append((Y[n]-m)*(np.sqrt(n+1)/sigma))
    
    
    
#     plt.figure()
#     #plt.plot(X,Y)
#     plt.plot(X,Z)
#     plt.show()


#Question2a(1000,0.5)
#####################################################################################



def Question2b(N,l):
    Y=[]
    X=[]
    Z=[]
    m=1/l   
    sigma=1/(l**2)
    for n in range(1,N+1):
        X.append(n)
        S=0
        for k in range(n):
            u=expo(l)
            S+=u/n
        Y.append(S)
    for n in range(N):
        Z.append((Y[n]-m)*(np.sqrt(n+1)/sigma))
    
    X=np.linspace(-20,20,N)
    W=np.zeros(N)
    for n in range(N):
        for k in range(N):
            if X[k]<=Z[n]<X[k+1]:
                W[k]+=1/N
    
    E=0
    V=0
    for k in range(N):
        E+=X[k]*W[k]
    print(f"On trouve une espérance expérimentale de {E}") 
    for k in range(N):
        V+=((Z[k]-E)**2)/N   
    print(f"On trouve une Variance expérimentale de {V}") 
    
                
    plt.figure()
    plt.bar(X,W)
    plt.show()
    
#Question2b(1000,0.5)                                   
    
    
#####################################################################################



def fInverse(p):
    return np.sqrt(p)

def f():
    return fInverse(random.random())


# def Question3a(N):
#     Y=[]
#     X=[]
#     Z=[]
#     m=2/3
#     sigma=1/18    ##par calcul
#     for n in range(1,N+1):
#         X.append(n)
#         S=0
#         for k in range(n):
#             u=f()
#             S+=u/n
#         Y.append(S)
#     for n in range(N):
#         Z.append((Y[n]-m)*(np.sqrt(n+1)/sigma))
    
    
    
#     plt.figure()
#     #plt.plot(X,Y)
#     plt.plot(X,Z)
#     plt.show()

#Question3a(1000)


def Question3b(N):
    Y=[]
    X=[]
    Z=[]
    m=2/3
    sigma=1/2    ##par calcul
    for n in range(1,N+1):
        X.append(n)
        S=0
        for k in range(n):
            u=f()
            S+=u/n
        Y.append(S)
    for n in range(N):
        Z.append((Y[n]-m)*(np.sqrt(n+1)/sigma))
    
    X=np.linspace(-20,20,1000)
    W=np.zeros(1000)
    for n in range(N):
        for k in range(1000):
            if X[k]<=Z[n]<X[k+1]:
                W[k]+=1/N
    
    E=0
    V=0
    for k in range(N):
        E+=X[k]*W[k]
    print(f"On trouve une espérance expérimentale de {E}") 
    for k in range(N):
        V+=((Z[k]-E)**2)/N   
    print(f"On trouve une Variance expérimentale de {V}") 
                
    plt.figure()
    plt.bar(X,W)
    plt.show()


#Question3b(1000)


#####################################################################################

"""Appel des methodes pour chaque question de l'exercice 4"""
print("-----EXERCICE 4----")
print("-----EX4_QUESTION 1b----")
print("\n")
print("")
time.sleep(1)
Question1b(1000,1000)
print("\n")
print("")
time.sleep(2)
print("Apuyer sur 'x' dans le clavier pour continuer à la question suivante")
if keyboard.read_key() == "x":
    print("-----EX4_QUESTION 2b----")
    print("\n")
    time.sleep(1)
    Question2b(1000,0.5)
    print("\n")
time.sleep(2)
print("Apuyer sur 'x' dans le clavixxxer pour continuer à la question suivante")
if keyboard.read_key() == "x":
    print("-----EX3_QUESTION 3b----")
    print("\n")
    print("Graphique de la courbe représentative de Sn/n en fonction de n pour la loi ayant comme fonction densité f("
          "x) = 2x définie sur [0;1]")
    time.sleep(1)
    Question3b(1000)
    print("\n")
print("FIN EXERCICE 4")








