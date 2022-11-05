#!/usr/bin/env python3

"""
Die Funktion remove_multiples(Liste, factor) löscht
    alle Vielfachen (element % factor == 0) und gibt die Liste zurück.
Ob sie dabei die Orginialliste modifiziert, ist euch überlassen, 
    findet es aber bitte heraus und schreibt es in die Dokumentation der Funktion!
    Wenn eure Funktion Elemente aus der Originalliste löscht, 
    solltet ihr ihr vermutlich nicht die mitgeben wie hier:
        remove_multiples(myList, 3)
    sondern eher so eine Kopie hineingeben:
        remove_multiples(myList[:], 3)
"""

def remove_multiples(Liste, factor):
    """Dokumentation: entfernt Vielfache von `factor` aus der `Liste`"""

    #Was sind verschiedene Probleme dieser Ansätze?
    #result.append(element)
    #Liste.remove(element)


    return Liste

"""
Hier könnt ihr selbst experimentieren, ob eure Funktion funktioniert
"""

myList = [1, 2, 3]
print(remove_multiples(myList, 3))

#löscht dieses exit, um meine Tests laufen zu lassen
exit(0)

"""
Hier wird von mir geprüft, ob die Funktion tut, was sie soll
Wenn die Datei check.py nicht im aktuellen Ordner liegt, müsst ihr das hier löschen
"""
from check import check
def test():
    print("Testing:")

    List = [1, 2, 3, 15, 6, 7, 8, 10, 9, 11, 14, 17]
    List_no3s = [1, 2, 7, 8, 10, 11, 14, 17]
    List_no5s = [1, 2, 3, 6, 7, 8, 9, 11, 14, 17]
    check(f"entferne aus {List} die Vielfachen von 3", remove_multiples(List[:], 3), List_no3s)
    check(f"entferne aus {List} die Vielfachen von 5", remove_multiples(List[:], 5), List_no5s)

if __name__ == '__main__':
    test()
