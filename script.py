import random
import string

def generate_password():
    # on utilise string.ascii_letters pour obtenir toutes les lettres
    letters = string.ascii_letters
    # on utilise string.digits pour obtenir tous les chiffres
    digits = string.digits
    # on utilise string.punctuation pour obtenir tous les caractères spéciaux
    punctuation = string.punctuation

    #on combine tout ça
    password_characters = letters + digits + punctuation

    #on génère ensuite un mot de passe à 8 caractères en combinant aléatoirement ces caractères
    strong_password = ''.join(random.choice(password_characters) for _ in range(8))

    return strong_password

def main():
    password = generate_password()
    print('Mot de passe', password)

if __name__ == "__main__":
    main()
