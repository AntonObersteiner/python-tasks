# Die Caesar-Chiffre ist eine ziemlich alte Verschlüsselung,
# die, wir ihr sehen werdet, recht leicht zu knacken ist.
# Verwandte Aufgabe: gene_*.py aus dem Ordner dict
# alle Eingabezeichen werden um einen festen Wert verschoben,
# z.B. ist "HALLO ZAZ" + 2 => "JCNNQ BCB"

def encrypt(text, shift):
    # ord(letter) -> ascii-zahl für den buchstaben
    # chr(zahl) -> ascii buchstabe
    # ASCII von 64+1 bis 64+26: A-Z
    # ASCII von 96+1 bis 96+26: a-z 
    #   (oder text.upper() verwenden)
    return text

def decrypt_easy(text, shift):
    # hier kann man auch einfach encrypt aufrufen, wenn das 
    # richtig implementiert wurde
    return text

# Wie kann man shift herausfinden?
# Was unterscheidet natürlich-sprachliche Texte (deutsch, englisch)
# von dem chaotischen Zeug, das bei allen anderen Shift-Werten rauskommt?
def decrypt(text):
    shift = 0
    return text, shift

def main():
    text = input("Type some text: ")
    shift = int(input("Type some integer: "))
    shifted = encrypt(text, shift)
    reversed_text_easy = decrypt_easy(shifted, shift)
    reversed_text, reversed_shift = decrypt(shifted)
    print(f"encrypted: {shifted}")
    print(f"decrypted easy: {reversed_text_easy}")
    print(f"shift analyzed: {reversed_shift}")
    print(f"decrypted: {reversed_text}")
    if reversed_shift != shift:
        print("It seems, your algorithm is not correct or your text is too short or too special.")
