"""
Hier soll eine Klasse entstehen, die einen Menschen repräsentiert
Der hat erstmal einen Vor- und einen Nachnamen
Aufgabe:
    speichert auch den Nachnamen
    Ergänzt vorstellen so, dass der Mensch seinen Namen nennt
Freie Aufgaben:
    fügt weitere Attribute hinzu (Alter, Eltern/Kinder, ...)
    erstellt eine Klasse 'Bar' mit einer Methode 'einlass',
        sodass man eine Bar erstellen und dann die Bar fragen kann, 
        ob sie einen bestimmten Menschen einlässt
        (entweder am Alter oder am sechsten Bustaben des Nachnamen)

z.B.:
maria = Mensch("Maria", "Stockhammer")
klaus = Mensch("Klaus", "Estak")

foo_bar = Bar()
foo_bar.einlass(maria) #-> True/False oder ein Text oder nur print
"""

class Mensch:
    #neuen Menschen mit Mensch(vorname, nachname) erzeugen
    #(namen sollten Strings sein)
    def __init__(self, first_name, last_name):
        #übergebenen Vornamen ins "Selbst" kopieren -> sich merken
        self.first_name = first_name

    #damit print(mensch) gut funktioniert
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def vorstellen(self):
        #Das ist bisschen kurz, und ohne den eigenen Namen
        return "Hi"



"""
Ab hier teste ich die Klasse darauf, ob sie kann, was sie soll
"""
questions = 0
def check(what_is, what_should_be, message):
    global questions
    if what_is != what_should_be:
        print(message, f"{what_is} != {what_should_be}")
        questions += 1

mensch1 = Mensch("Henriette", "Bora")
try:
    check(mensch1.first_name, "Henriette", "self.first_name wurde für mensch1 nicht auf 'Henriette' gesetzt?")
    check(mensch1.last_name,  "Bora",      "self.last_name wurde für mensch1 nicht auf 'Bora' gesetzt?")
except AttributeError as ae:
    print("Deine Klasse hat in __init__ irgendein self.... nicht angelegt:\n", ae, "\n\n")

mensch2 = Mensch("Steffen", "Merter")

what_steffen_says = mensch2.vorstellen()
print(f"{mensch2}: {what_steffen_says}")
if len(what_steffen_says) < 10:
    print("Das ist aber eine kurze Begrüßung...")
if mensch2.first_name not in what_steffen_says:
    print("Begrüßung ohne Vornamen?")
if mensch2.last_name not in what_steffen_says:
    print("Begrüßung ohne Nachnamen?")

print("Wenn drüber dieser Ausgabe nichts steht, ist die Aufgabe gelöst...")
