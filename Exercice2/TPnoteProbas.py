import random
import math
import numpy as np
import matplotlib.pyplot as plt


##Exercice 1

##Q1

def Bernoulli(p):
    X=random.random()
    if X<p:
        return 1
    else:
        return 0


def testBernoulli(p,lance):
    
    E=0

    ##Vérification espérance
    for k in range(lance):
        X=Bernoulli(p)
        E+=X/lance
    print(f"l'espérance doit valoir {p} on trouve {E} pour {lance} lancés ")

    var=0
    ##Vérification Variance
    for k in range(lance):

        X=Bernoulli(p)
        var+=((X-E)**2)/lance
    print(f"la variance doit valoir {p*(1-p)} on trouve {var} pour {lance} lancés ")
    
    
#testBernoulli(1/2,1000)


#########################################################################################
##Q2

def Binomiale(n,p):
    
    X=0
    for k in range(n):
        X+=Bernoulli(p)
        
    return X

def factorielle(n):
    p=1
    if n==0:
        return p
    for k in range(1,n+1):
        p*=k
    return p
        

def Parmi(k,n):
    return factorielle(n)/(factorielle(n-k)*factorielle(k))
    
    
    
def TestBinomiale(n,p,j):
    tabSimu=[]
    tabTheo=[]
    for k in range(n):
        tabTheo.append(Parmi(k,n)*(p**k)*(1-p)**(n-k)*100)
        tabSimu.append(0)
    
    # for i in range(j):
    #     X=Binomiale(n,p)
    #     for k in range(n):
    #         if X==k+1:
    #             tabSimu[k]+=(1/j)*100
    ##en pourcentage 
    for i in range(j):
        X=Binomiale(n,p)
        
        for k in range(n):
            if X==k+1:
                tabSimu[k]+=1
    
    ##Espérance
    E=0
    for k in range(n):
        E+=(tabSimu[k])*(k+1)/j
        
    print(f"L'espérance doit théoriquement valoire {n*p} On trouve {E}")
    
    ##Variance
    v=0
    for k in range(n):
        v+=(tabSimu[k])*(((k+1) -E)**2)/j
    print(f"La variance doit théoriquement valoire {n*p*(1-p)} On trouve {v} ")
                

    
    
#TestBinomiale(10,1/2,10000)    



    
#########################################################################################
##Q3


def geometrique2(p):
    if p<0 or p>1:
        return "Erreur p doit appartenir à [0,1]"
    u=random.random()
    x=1
    pk=p
    F=pk
    while(u>F):
        x+=1
        pk=pk*(1-p)
        F=F+pk
    return x

#print(geometrique2(0.5,100))

def TestGeo(p,j):
    somme=0
    v=0
    for i in range(j):
        somme+=geometrique2(p)/j
    print(f"On doit théoriquement trouver une espérance de {1/p} On trouve {somme} ")
    
    for i in range(j):
        v+= ((geometrique2(p)-somme)**2)/j
    print(f"On doit théoriquement trouver une variance de {(1-p)/(p**2)} On trouve {v} ")
        
#TestGeo(0.7,1000)
        
    
        



#########################################################################################
#Q4

def UniformeDiscret(a,b):
    if a>b:
        return("Erreur il faut a<b")
    return math.floor(a+(b-a+1)*random.random())



def TestUniformDiscrete(n,j):           
    X=0
    
    
    if(n<2):
        return("Erreur il faut choisir n>=2")
    for k in range(2,n+1):
        somme=0
        Vt=0
        for i in range(j):
            X=UniformeDiscret(1,k)
            somme+=X/j
        
        for i in range(j):
            X=UniformeDiscret(1,k)
            Vt+=((X-somme)**2)/j
            
            
        E=(1+k)/2
        V=((k**2)-1)/12
        
        print(f"Pour k={k} et j={j} On doit théoriquement trouver une espérance de E={E} et une variance de V={V}\n On trouve Et={somme}  et Vt={Vt} \n\n ")
        

    
    
#TestUniformDiscrete(5,1000)





##Q5




def UniformeContinue(a,b):
    if a>b:
        return("Erreur il faut a<b")
    return a+(b-a)*random.random()



def testUniformeContinue(n):
    somme=0
    V=0
    for k in range(n):
        X=UniformeContinue(-1,1)
        somme+=X/n
    for k in range(n):
        X=UniformeContinue(-1,1)
        V+=((X-somme)**2)/n
        
        
    print(f"L'espérance doit théoriquement valoire 0, on trouves {somme} pour n={n}")
    print(f"La Variance doit théoriquement valoire 1/3 , on trouves {V} pour n={n}")

    
    
#testUniformeContinue(1000)


def traceUniformeContinue(n,j):
    X1=np.linspace(-1,1,n)
    Y=np.zeros(n)
    for i in range(j):
        X2=UniformeContinue(-1,1)
        for k in range(n):
            if X1[k]<=X2<X1[k+1]:
                Y[k]+=1
    
    plt.figure()
    plt.plot(X1,Y)
    plt.show()

#traceUniformeContinue(100,10000)



#########################################################################################


#########################################################################################


##Exercie 2
           
#Q1   

def fonctionDiscrete(X, n, P):
    """Tableau X trié par odre croissante"""
    """Tab X et Tab P même taille"""
    """P(X<x1)=p1=0"""
    u = random.random()
    i = 1
    F = P[0]
    while (i < n and u > F):
        i += 1
        F = F + P[i]

    if (u > F):
        return False     #Indéfini
    else:
        x = X[i]
    return x




def BernouilliDiscret(p):
    X=[0,1]
    P=[1-p,p]
    return fonctionDiscrete(X,1,P)


print(BernouilliDiscret(0.5))

def TestBernouilliInverse(p,n):
    E=0
    V=0
    for k in range(n):
        E+=BernouilliDiscret(p)/n
    for k in range(n):
        V+=((BernouilliDiscret(p)-E)**2)/n
    print(f"l'espérance doit valoir {p} on trouve {E} pour {n} lancés ")
    print(f"la variance doit valoir {p*(1-p)} on trouve {V} pour {n} lancés ")
    
    
    
#TestBernouilliInverse(1/2,100)





#########################################################################################

#Q3




def poisson(l):
    if (l>0):
        u=random.random()
        x=0
        pk=np.exp(-l)
        F=pk
        while(u>F):
            x+=1
            pk=pk*l/x
            F+=pk
        return x











        
        
def PoissonDiscret(l,n):
    X=[]
    P=[]
    for k in range(1,n+1):
        X.append(k)  
        P.append(np.exp(-l)*(l**k)/factorielle(k))
    return fonctionDiscrete(X,n-1,P)



    
def TestPoissonDiscret(l,n,j):
    E=0
    c=0
    V=0
    for i in range(j):
        if(PoissonDiscret(l,n)!=False):
            E+=PoissonDiscret(l,n)
            c+=1
    E=E/c
    c=0
    for i in range(j):
        if(PoissonDiscret(l,n)!=False):
            V+=(PoissonDiscret(l,n)-E)**2
            c+=1
    V=V/c
    print(f"On devrait théoriquement trouver E={l}, on trouve E={E}") 
    print(f"On devrait théoriquement trouver V={l}, on trouve V={V}") 
    
     
    
    
    
# def TestPoissonDiscret(l,n,j):
#     E=0
#     V=0
#     for i in range(j):
#         if(PoissonDiscret(l,n)!=False):
#             E+=PoissonDiscret(l,n)/j
            
#     for i in range(j):
#         if(PoissonDiscret(l,n)!=False):
#             V+=((PoissonDiscret(l,n)-E)**2)/j
#     print(f"On devrait théoriquement trouver E={l}, on trouve E={E}") 
#     print(f"On devrait théoriquement trouver V={l}, on trouve V={V}") 
    
    
    
    
    
    
        
TestPoissonDiscret(0.5,160,100) 
  
   
        
#########################################################################################   
        

        
        
        
        
        
        
        