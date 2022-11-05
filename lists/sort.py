#!/usr/bin/env python3

"""
In dieser Aufgabe wird eine Liste von sortierbaren Objekten
    z.B. int, float, string
sortiert.
Dazu wird die Funktion sort(L) definiert,
    die die überreichte Liste L direkt sortiert. (also keine Kopie anfertigt)
"""

def sort(List):
    #sort here
    return List

"""
Hier könnt ihr selbst experimentieren, ob eure Funktion funktioniert
"""

L = [1, 4, 3, 2]
sort(L)
print(L)

#löscht dieses exit, um meine Tests laufen zu lassen
exit(0)

"""
Hier wird geprüft, ob die Funktion tut, was sie soll
"""
from check import check
def test():
    print("Testing:")

    Z_origin = [5, 7, 2, 1]
    Z_sorted = [1, 2, 5, 7]
    F_origin = [2.0, 7.4, 2.0, 1.0]
    F_sorted = [1.0, 2.0, 2.0, 7.4]
    S_origin = ["5", "sieben", "aaba", "aaa"]
    S_sorted = ["5", "aaa", "aaba", "sieben"]
    L_origin = [Z_sorted, F_sorted]
    L_sorted = [F_sorted, Z_sorted]

    check("Integer", sort(Z_origin), Z_sorted)
    check("Floats",  sort(F_origin), F_sorted)
    check("Strings", sort(S_origin), S_sorted)
    check("Listen",  sort(L_origin), L_sorted)

    check("Leere?", sort([]), [])

if __name__ == '__main__':
    test()
