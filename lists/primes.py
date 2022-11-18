#!/usr/bin/env python3

"""
In dieser Aufgabe werden die Primzahlen bis zu einer Zahl bestimmt.
Dafür wird die Funktion primes(up_to) definiert, die eine Liste zurückgibt.
Ein effizienter Algorithmus wird in primes_alg.txt erklärt,
    wer selber knobeln will, macht das :)
"""

#man kann die vorher gelöste Aufgabe hier wiederverwenden
#das hier führt die Datei multiples.py aus 
#und gibt uns dann die Funktion remove_multiples daraus
from multiples import remove_multiples

def primes(up_to = 1000):
    #the numbers from 2 to N=up_to are probably a good start
    candidates = list(range(2, up_to + 1))
    #Tipp:
    #   n % p  ergibt den Rest  n mod p
    #   wenn n % p == 0, dann gilt: p teilt n

    return candidates

"""
Hier wird geprüft, ob die Funktion tut, was sie soll
"""
from check import check
def test():
    print("Testing:")

    check("bis 1:", primes(1), [])
    check("bis 10:", primes(10), [2, 3, 5, 7])
    check("bis 100:", primes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    test()

