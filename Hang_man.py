import random
from display_hang import display_game
from word_page import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Juguemos el Ajorcao")
    print(display_game(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Por favor ingrese una letra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ya adivinaste esa letra, intenta otra", guess)
            elif guess not in word:
                print(guess, "no esta en la palabra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Muy bien,", guess, "esta en la palabra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ya adivinaste la palabra", guess)
            elif guess != word:
                print(guess, "no es la palabra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("No es valido.")
        print(display_game(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Adivinaste! felicidades!")
    else:
        print("Agostaste todas tus opciones, la palabra era " + word +".")



def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()