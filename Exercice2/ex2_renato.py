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
    i = 1
    F = P[0]
    while (i < n and u > F):
        i += 1
        F = F + P[i]

    if (u > F):
        return "indefini"
    else:
        x = X[i]
    return x


def poisson(l):
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



def fonctionGeometrique(p):
    if 0 < p < 1:
        u = rd.random()
        x = 1
        pk = p
        F = pk
        while (u > F):
            x += 1
            pk = pk * (1 - p)
            F = F + pk
        if (x > 0):
            return x
        else:
            return 'indefini'

def G_question4(p, l):
    return - ((1 / l) * np.log(1 - p))


def expo(l):
    return G_question4(rd.random(), l)


def question1():
    pass


def question2():
    print("LOI GEOMETRIQUE de parametre p")
    p=5

    print("E[X] theorique = 1/p = 1/"+str(p) +" = " + str(1/p))
    print("Var(X) theorique = (1-p) / (p²) = 1-" + str(p) + " / " + str(p*p) + " = " + str(((1-p) / (p*p))))


def question3():
    print("LOI de POISSON de parametre lambda")
    l = 5
    x = poisson(l)
    print("E[X] theorique = lambda = " + str(l))
    print("Var(X) theorique = lambda = " + str(l))
    print("Apres calcul fonctionPoisson : " + str(x))


def question4():
    """Exponentielle de parametre lamda"""
    print("On considere lamda > 0 et X, une variable aleatoire de loi exponentielle(lamda")
    """/////////////////////////////////"""
    """on prend le parametre lambda 1"""
    print("pour  lambda = 1\n")
    l = 1
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
print("-----QUESTION 2----")
print("\n")
question2()
print("\n")
print("-----QUESTION 3----")
print("\n")
question3()
print("\n")
print("-----QUESTION 4----")
print("\n")
question4()
print("\n")

# pour une loi discrete(bernoulli?)
# l=2
# X = np.linspace(0, 10, 100)
# """print("Table des probabilitées X")"""
# """print(X)"""
# """P tab/liste contenant les probabilités de P(X=xi)"""
# P = []
# for i in X:
#   result = poisson(l)
#   P.append(result)
# """print("Table des probabilitées P")"""
# """print(P)"""
