#!/usr/bin/env python3

"""
In diesem Programm sollen einige Nutzer-Ein- und- Ausgaben getätigt werden.
Es soll dabei frei einstellbare Sprachen haben (Bisher: deutsch, französisch)
    Die übliche Technik hier wäre, alle Texte mit einem key zu versehen,
        damit man sie aus verscheidenen Sprachen abrufen kann.
Testet das Programm, lest es dann. Ändert die Sprache im Code. Stellt Fragen.

Fügt eine Sprache und eine Ausgabe hinzu. Z.B. steht aktuell noch nirgends,
    dass man das Programm mit 'quit' schließt.
        fr: "Pour quitter le programme, tapez 'quit'"
    Vielleicht macht ihr Übersetzungen für 'quit' in die anderen Sprachen?

Aktuell kann man die Sprache nur im Code ändern.
    Wie könnte die Sprache von außen eingestellt werden?
Eine Option:
    Unten werden die Kommandozeilen-Argumente geladen und ausgegeben.
    Sorgt dafür, dass beim Argument '--de' Deutsch und
        beim Argument '--fr' Französisch verwendet wird (etc).
    Cool wäre, wenn ihr dafür ein dict verwendet,
        statt vielen if-s und elif-s...
"""

de = {
    #Struktur der Zeilen:
    #allgemeiner Key: Sprach-spezifischer Text
    "intro": "Dies ist ein kleiner Taschenrechner in Python.",
    "input_prompt": "Berechnung: ",
}
fr = {
    "intro": "Ceci est un petit calculateur, écrit en Python.",
    "input_prompt": "Calculation: ",
}

def main(lang):
    print(lang["intro"])

    #loop forever
    while True:
        #ask user for input
        inp = input(lang["input_prompt"])

        if inp == "quit":
            break

        try:
            #Python evaluiert den Ausdruck (z.B. "5 + 8" oder "17.5 ** 3" oder "'Mara', 'Karl'")
            #Ist das sicher? Wie könnte man das kuputtmachen?
            print("->", eval(inp))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    from sys import argv

    #hier kann die Sprache eingestellt werden
    lang = de

    for arg in argv:
        print(f"Arg {argv.index(arg)}: {arg}")

    #hier wird diese Einstellung an die main-Funktion übergeben
    main(lang)
