"""np.log is ln, whereas np.log10 is your standard base 10 log."""
"""Ne pas mettre "self" comme argument des methodes"""
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

def fonctionDiscrete(X, n, P):
    """Tableau X trié par odre croissante"""
    """Tab X et Tab P même taille"""
    """P(X<x1)=p1=0"""
    u = rd.rand()
    i=1
    F=P[0]
    while(i<n and u>F):
        i+=1
        F = F + P[i]

    if (u>F):
        print("Loi de poisson :  X est indefini")
        return "indefini"
    else:
        x = X[i]
    return x




def G_question4(p,l):
    return - ((1 / l) * np.log(1 - p))


def expo(l):
    return G_question4(rd.random(),l)


def question1():
    pass


def question2():
    pass


def poisson(l):
    """P(X=l)"""
    if (l > 0):
        u = rd.random()
        x = 0
        pk = np.exp(-l)
        F = pk
        while (u > F):
            x += 1
            pk = pk * l / x
            F += pk
        return x

def question3():
    l=2
    X = np.linspace(0, 10, 100)
    """print("Table des probabilitées X")"""
    """print(X)"""
    """P tab/liste contenant les probabilités de P(X=xi)"""
    P = []
    for i in X:
        result = poisson(l)
        P.append(result)
    """print("Table des probabilitées P")"""
    """print(P)"""
    x = fonctionDiscrete(X,100,P)
    if x=="indefini":
        print("X non defini")
    else:
        print("FonctionDiscretePoisson : " + str(x))


def question4():
    """Exponentielle de parametre lamda"""
    print("On considere lamda > 0 et X, une variable aleatoire de loi exponentielle(lamda")
    """/////////////////////////////////"""
    """on prend le parametre lambda 1"""
    print("pour  lambda = 1\n")
    l=1
    X = np.linspace(0, 4, 100)
    Y = np.zeros(100)
    j = 10000
    for i in range(j):
        for k in range(100):
            if k <= expo(l) < k + 1:
                Y[k] += 1 / j

        # Create bars
    """print(max(Y))"""
    plt.figure()
    plt.bar(X, Y)
    plt.show()


"""Appel des methodes pour chaque question de l'exercice2"""
print("-----QUESTION 3----")
print("\n")
question3()
print("\n")
print("-----QUESTION 4----")
print("\n")
question4()
print("\n")
