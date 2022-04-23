import math
def oblicz_newtona(a , b):
    licznik = math.factorial(a)
    mianownik = math.factorial(b)*math.factorial(a-b)
    return int(licznik/mianownik)
liczby = input()
liczby = liczby.split()
for i in range(len(liczby)):
    liczby[i] = int(liczby[i])
print(oblicz_newtona(liczby[0],liczby[1]))
