"""np.log is ln, whereas np.log10 is your standard base 10 log."""
"""Ne pas mettre "self" comme argument des methodes"""
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import keyboard
import time

#import de methodes d'inversion codés dans le fichier de l'exercice 1
from TPnoteProbas import fonctionDiscrete
from TPnoteProbas import BernouilliDiscret
from TPnoteProbas import TestBernouilliInverse
from TPnoteProbas import geometriqueDiscret
from TPnoteProbas import TestGeoInverse


def factorielle(n):
    f = 1
    for k in range(1, n + 1):
        f *= k
    return f


def discrètePoisson(l, n):
    X = []
    P = []
    for k in range(n):
        X.append(k)
        P.append(np.exp(-l) * (l ** k) / factorielle(k))
    return fonctionDiscrete(X, n, P)


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

def G_question4(p, l):
    return - ((1 / l) * np.log(1 - p))


def expo(l):
    return G_question4(rd.random(), l)


def question1():
    print("LOI DE BERNOULLI de parametre p")
    TestBernouilliInverse(1 / 2, 100)


def question2():
    print("LOI GEOMETRIQUE de parametre p")
    """0<p<1"""
    p = 0.5 #probabilité de succées

    TestGeoInverse(p,100,1000)
    print("E[X] theorique = 1/p = 1/" + str(p) + " = " + str(1 / p))
    print("Var(X) theorique = (1-p) / (p²) = 1-" + str(p) + " / " + str(p * p) + " = " + str(((1 - p) / (p * p))))



def question3():
    print("LOI de POISSON de parametre lambda")
    l = 0.5
    #x = discrètePoisson(l, 100)
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
    plt.plot(X, Y)
    plt.show()


"""Appel des methodes pour chaque question de l'exercice2"""
print("-----QUESTION 1----")
print("\n")
question1()
print("\n")
print("")
time.sleep(3) #on attend 3 secondes avant de pouvoir passer à la question precedente
#cela évite les affichages des graphiques d'autres questions
print("Apuyer sur 'x' dans le clavier pour continuer à la question suivante")
if keyboard.read_key() == "x":
    print("-----QUESTION 2----")
    print("\n")
    question2()
    print("\n")
time.sleep(3)
print("Apuyer sur 'x' dans le clavier pour continuer à la question suivante")
if keyboard.read_key() == "x":
    print("-----QUESTION 3----")
    print("\n")
    question3()
    print("\n")
time.sleep(3)
print("Apuyer sur 'x' dans le clavier pour continuer à la question suivante")
if keyboard.read_key() == "x":
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
