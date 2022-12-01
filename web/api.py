import requests
import json

''' 
1.) frag die Sport-Traingings-API nach Übungen für den Bizeps.
        -> wie viele Übungen gibt es, für die ihr kein Equipment braucht? 
        
2.) Frag die Sport-Traingings-API nach Übungen für verschiedene Muskelgruppen (zB. chest, biceps, forearmes, lower_back, ...)
    und speichere die Antwort in einer JSON Datei mit den Muskeln als keys.
    Aber bitte chillt mit der anzahl an Anfragen!!! der API key lässt nicht unbegrenzt Anfragen pro Tag durch und es soll für alle reichen
    
    in etwa so:
    {
        "chest" :      { ... },
        "lower_back" : { ... },
        "biceps" :     { ... },
    }

3.) stelle eine Anfrage an eine beliebige API (von der verlinkten Seite) und filtere sinnvolle Attribute
3b) ändere den Code so, dass du die Antwort als JSON-Datei abspeicherst und die Daten daraus holst

TIPP: 
    I) die Anfrage ist so aufgebaut: 
        antwort = requests.get("die-entsprechende-url.com", headers)
            
    II) manche Fragen klärt das cheatsheet : https://github.com/AntonObersteiner/python-cheatsheet/blob/master/cheatsheet.pdf

    III) für json
        import json
        
        # LESEN (json datei zu dictionary)
        with open("example.json", "r") as fd:
            data = json.load(fd)
        # SCHREIBEN (dictionary zu json datei)
        data = {...}
        with open("example.json", "w") as fd:
            json.dump(data, fd)
'''


'''https://api-ninjas.com/api/exercises'''


headers = {
    'X-Api-Key': 'MjH2qN81hsSnBYyGXPFfHg==CGrfVbMqVQRuN555'
}
