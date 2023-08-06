from words import word_bank
import random 

def instructions():
    print("""Wordle is a single player game. 
    You have 6 attempts to guess a 5-letter hidden word.
    🟩 indicates the letter is correct and in position.
    ⬛indicates that the letter isn't in the word at all.
    🟨 indicates that the letter is in the word but is in the wrong position.
    """)

    
instructions()

dictionary = word_bank
def check_word():
    hidden_word = random.choice(dictionary)
    hidden_word = hidden_word.lower()

    # For Testing
    # print(hidden_word)

    attempts = 6
    while attempts > 0:
        guess = str(input("Guess the word: "))
        guess = guess.lower()

        # Correct Guess
        if guess == hidden_word:
            print("Correct!")
            break

        # If the guess is too long or not long enough.
        elif len(guess) != len(hidden_word):
            print("Not a 5-letter word. Try again.")

        # Incorrect Guess
        else:
            attempts = attempts - 1
            print(f"Guess again. You have " + str(attempts) + " attempt(s) left. \n")
            for i, j in zip(hidden_word, guess):
                # if the letter is in the word and in the correct spot
                if j in hidden_word and j in hidden_word[hidden_word.index(i)]:
                    print(j+ " 🟩 ") 
                # if the letter is in the word, wrong spoit
                elif j in hidden_word:
                    print(j+ " 🟨 ") 
                # letter not in word
                else:
                    print(" ⬛ ")
    # Game Over                
    if attempts == 0:
        print(f"Game over. The word was " + hidden_word + ".")

check_word()


