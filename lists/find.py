#!/usr/bin/env python3

"""
Hier sollen Funktionen entstehen,
    die erkennen, wo etwas in einer Liste ist.
find_first(List, element) ergibt den Index des ersten Auftretens
find_nth(List, element, n) findet das n-te Auftreten von element
"""

def find_first(List, element):
    for index in range(len(List)):
        pass
    return 0

def find_nth(List, element, n = 1):
    return 0

"""
Ab hier wird geprüft, ob die Funktion tut, was sie soll
"""

from check import check, check_error
def test():
    Zahlen = [1, 2, 5, 7, 5]
    #Index:   0  1  2  3  4

    def test_normal():
        first_5_at = find_first(Zahlen, 5)
        second_5_at = find_nth( Zahlen, 5, 2)

        check("finde erste  5", first_5_at, 2)
        check("finde zweite 5", second_5_at, 4)

    def test_weird(cannot_find_return = None):
        """
        Wie reagiert eure Funktion bei falscher Benutzung?
        Gibt sie None zurück oder schmeißt sie einen Fehler?
            raise ValueError(f"There is no '{element}' in '{Liste}'!")
        beziehungsweise
            raise ValueError(f"There is no {n}-th '{element}' in '{Liste}'!")
        """

        # check(      "finde nullte  1", find_nth(  Zahlen, 1, 0), None)
        # check(      "finde nullte  3", find_nth(  Zahlen, 3, 0), None)

        if cannot_find_return == None:
            check(      "finde erste  3", find_first(  Zahlen, 3   ), None)
            check(      "finde dritte 5", find_nth(    Zahlen, 5, 3), None)
        elif isinstance(cannot_find_return, Exception):
            check_error("finde erste  3", find_first, (Zahlen, 3   ), ValueError)
            check_error("finde dritte 5", find_nth,   (Zahlen, 5, 3), ValueError)
        else:
            check(      "finde erste  3", find_first(  Zahlen, 3   ), cannot_find_return)
            check(      "finde dritte 5", find_nth(    Zahlen, 5, 3), cannot_find_return)

    print("Testing:")
    print(f"mit Liste: {Zahlen}")

    test_normal()
    test_weird(None)


if __name__ == '__main__':
    test()
