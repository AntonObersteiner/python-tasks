#!/usr/bin/env python3

"""
Erklärung in gene_explanation.txt
"""

#vordefinierte Daten
from gene_data import amino_to_dna, abbrev


def load(file_name):
    #Datei öffnen, auslesen und schließen.
    #Dann gelesenen Inhalt zu Großbuchstaben machen (Internet-Recherche oder fragen oder selber rausfinden)
    #Inhalt zurückgeben
    return "AUGGCCCAGGCT"

def translate(dna_text):
    #entweder mit amino_to_dna oder
    #mit eigener Datenstruktur,
    #   die man einmal generiert (z.B. in gene_data.py)
    return "MetAlaGlnAla"

def substring(string, start = 0, stop = None):
    #gibt standardmäßig den ganzen String zurück
    if stop is None:
        stop = len(string)

    #wenn jetzt start oder stop nicht im Bereich  [0, len(string) - 1]  liegen,
    #sollte kein Fehler passieren, sondern die Funktion sollte das anpassen und das mögliche ausgeben

    return string[start:stop]

def match(dna_text, to_match):
    #wo ist to_match in dna_text?
    index = 0

    #wie häufig weicht das dort dann ab?
    mutations = 0

    return index, mutations

def print_match(dna_text, to_match):
    index, mutations = match(dna_text, to_match)
    print(f"DNA {dna_text} contains {to_match} at {index} (mutations: {mutations})")

def count_aminos(dna_text, start = 0):
    return {"Ala": 0, "Val": 0}

def compare_count(count1, count2):
    similarity = 0
    return similarity

def replace(dna_text, to_remove, to_insert, start = 0):
    """
    jedes  to_remove  mit  to_insert  ersetzen
    vorsicht:
        AAAG  und AAGG  enthalten beide AAG,
        aber wenn die dreier-Sätze so geteilt werden (start = 0):
            AAA|G  und  AAG|G  wird klar, dass nur im zweiten ersetzt werden darf
        bei start = 1 dagegen:
            (A)AAG  und  (A)AGG  darf nur im ersten ersetzt werden kann
    """

    return dna_text


def main(file_name = "TEST.dna"):
    dna_text = load(file_name)
    translation = translate(dna_text)

    #wenn ihr große Strings (z.B. HEXA.dna) ausgebt, könnt ihr substring oder etwas ähnliches verwenden.
    #Aber substring("ACAC", 0, 100) muss erst zum Funktionieren gebracht werden
    print(f"translation of {dna_text}: {translation}")


    print_match(dna_text, "CCCAG")
    #sollte 4 sein, mit 0 Mutationen

    print_match(dna_text, "CCTAG")
    #sollte 4 sein, mit 1 Mutation


    for start in range(0, 3):
        print(f"Anzahl der jeweiligen Aminosäuren bei start = {start}: {count_aminos(dna_text, start)}")
    #das kann man jetzt mit Hand mit den Daten in gene_distr.txt vergeleichen
    #oder man rechnet aus, wie ähnlich sie sind
    #Recherche oder Fragen: Mittlere Quadratische Abweichung oder Mean Square Error


    #Womit können alle GCT ersetzt werden, dass immer noch Ala rauskommt?
    replace(dna_text, "GCT", "???", 0)

    print(f"Ersetzungen von 'GGC' in '{dna_text}':")
    print(f"    start at 0: '{replace(dna_text, 'GGC', '!!!', 0)}'")
    print(f"    start at 1: '{replace(dna_text, 'GGC', '!!!', 1)}'")
    print(f"    start at 2: '{replace(dna_text, 'GGC', '!!!', 2)}'")

if __name__ == '__main__':
    from sys import argv
    print(f"Kommando-Zeilen-Argumente: {argv}")
    #verwendet mal:  python3 gene_expr.py bli bla
    #statt nur:      python3 gene_expr.py
    #das wäre ein Weg, die Datei auf etwas anderes als "TEST.dna" einzustellen

    file_name = "TEST.dna"
    main(file_name)
