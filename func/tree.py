"""
Aufgabe hier ist, einen Baum mit Rekursion zu zeichnen.
dazu benötigt man eine Funktion, die mit der Turtle etwas zeichnet,
    aber am nach einem Funktions-Durchlaufs endet, wo sie begonnen hat.
Dadurch kann man dann mitten in dieser Form wieder die Funktion aufrufen
    und ein beliebig detailliertes Bild bekommen.
"""

import turtle

#schnelle Turtle
# turtle.speed(0)
# turtle.delay(0)

#wenn man das verwendet:
# turtle.tracer(0, 0)
#muss man jedes mal
# turtle.update()
#verwenden, wenn man etwas sehen möchte

def segment(depth = 0):
    print(f"{' '*depth}Tiefe: {depth}")
    #draw
    segment(depth + 1)
    #draw
    segment(depth + 1)
    #draw

if __name__ == '__main__':
    segment()
