# Die Caesar-Chiffre ist eine ziemlich alte Verschlüsselung,
# die, wir ihre sehen werden, recht leicht zu kancken ist.
# Verwandte Aufgabe: gene_*.py aus dict
# alle Eingabezeichen werden um einen festen Wert verschoben,
# z.B. ist "HALLO ZAZ" + 2 => "JCNNQ BCB"

def encrypt(text, shift):
    # ord(letter) = ascii-zahl für den buchstaben
    # chr(zalh) = ascii buchstabe
    # ASCII von 65 bis 65+26: A-Z
    # ASCII von 97 bis 97+26: a-z (oder text.upper() verwenden)
    return text

# Wie kann man shift herausfinden?
def decrypt(text):
    shift = 0
    return text, shift

def main():
    text = input("Type some text: ")
    shift = int(input("Type some integer: "))
    shifted = encrypt(text, shift)
    reversed_text, reversed_shift = decrypt(shifted)
    print(f"encrypted: {shifted}")
    print(f"shift analyzed: {reversed_shift}")
    print(f"decrypted: {reversed_text}")
    if reversed_shift != shift:
        print("It seems, your algorithm is not correct or your text is too short or too spcial.")
