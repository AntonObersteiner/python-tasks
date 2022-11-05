"""
Hier sollen einige Aufgaben zu Rekursion gelöst werden
1. Fibonacci-Zahlen:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    Summe der letzten zwei ergibt die nächste
2. Quicksort:
    Trenn-Element wählen
    in kleiner/gleich/größer sortieren
    die jeweils mit quicksort sortieren
    zusammenfügen
"""

def fibonacci(n):
    return n

def quicksort(Liste):
    return Liste


"""
Tests
"""
def check(test_name, what_is, what_should_be):
    if what_is != what_should_be:
        filler = " " * len(test_name + ": ")

        print(f"{test_name}: Funktion ergibt: {what_is}")
        print(f"{filler}Sollte sein:     {what_should_be}")
    else:
        print(f"{test_name} passed! :)")

def test_fibonacci():
    f = lambda n: n if n <= 1 else f(n - 1) + f(n - 2)
    for n in [0, 1, 2, 3, 4, 5, 10, 20]:
        check(f"Fibonacci-Zahl {n}", fibonacci(n), f(n))

def test_quicksort():
    Z_origin = [5, 7, 2, 1]
    Z_sorted = [1, 2, 5, 7]
    F_origin = [2.0, 7.4, 2.0, 1.0]
    F_sorted = [1.0, 2.0, 2.0, 7.4]
    S_origin = ["5", "sieben", "aaba", "aaa"]
    S_sorted = ["5", "aaa", "aaba", "sieben"]
    L_origin = [Z_sorted, F_sorted]
    L_sorted = [F_sorted, Z_sorted]

    check("Integer", quicksort(Z_origin), Z_sorted)
    check("Floats",  quicksort(F_origin), F_sorted)
    check("Strings", quicksort(S_origin), S_sorted)
    check("Listen",  quicksort(L_origin), L_sorted)

    check("Leere?", quicksort([]), [])

if __name__ == '__main__':
    test_fibonacci()
    test_quicksort()
