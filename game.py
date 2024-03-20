import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
# max_attempts = 10

# CONTADOR DE ERRORES
errores = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")


# AGREGO ELECCION DE DIFICULTAD
dificultad = int(input(f'Ingrese el nivel de Dificultad: (1- Facil 2- Media 3- Dificil) \n'))

match dificultad:
    case 1:
        print("dificultad facil")
        guessed_letters = ['a','e','i','o','ó','u']
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")

        word_displayed = "".join(letters)
    case 2:
        print("dificultad media")
        guessed_letters = [secret_word[0],secret_word[-1]]
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")

        word_displayed = "".join(letters)

    case 3:
        print("dificultad dificil")
        word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed}")

while errores < 5:
    # Pedir al jugador que ingrese una letra
    print(f"errores: {errores}")
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # EVITA EL BUG DEL STRING VACIO 
    if letter == "":
        print("Por favor ingrese una letra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    #Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if (letter in secret_word) and (letter != ""):
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        errores += 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has llegado a tus {errores} errores.")
    print(f"La palabra secreta era: {secret_word}")
