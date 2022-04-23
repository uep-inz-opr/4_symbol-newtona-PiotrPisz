import math
def oblicz_newtona(a , b):
    mianownik = math.factorial(a)
    licznik = math.factorial(b)*math.factorial(a-b)
    return mianownik/licznik
liczby = input()
liczby = liczby.split()
for i in range(len(liczby)):
    liczby[i] = int(liczby[i])
oblicz_newtona(liczby[0],liczby[1])
