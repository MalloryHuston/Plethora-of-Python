# Python Program to illustrate Hangman Game
import random

# List of words
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

# Split words into a list
someWords = someWords.split(' ')
word = random.choice(someWords)  # Randomly choose a secret word

def display_current_state(word, guessed_letters):
    """Display the current state of the word with guessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    # Display initial state
    print(display_current_state(word, []))

    playing = True
    guessed_letters = set()  # Track guessed letters
    chances = len(word) + 2  # Allow a few extra chances
    correct_guesses = 0

    try:
        while chances > 0:
            guess = input('Enter a letter to guess: ').strip().lower()

            # Validate the guess
            if not guess.isalpha() or len(guess) != 1:
                print('Please enter a single letter.')
                continue

            if guess in guessed_letters:
                print('You have already guessed that letter.')
                continue

            # Add the guess to the set of guessed letters
            guessed_letters.add(guess)

            # If the letter is in the word
            if guess in word:
                print(f"Correct! The letter '{guess}' is in the word.")
                correct_guesses += word.count(guess)
            else:
                print(f"Wrong guess! The letter '{guess}' is not in the word.")
                chances -= 1

            # Display current state of the word
            print(display_current_state(word, guessed_letters))
            print(f"Chances left: {chances}")

            # Check if the user has guessed the word
            if all(letter in guessed_letters for letter in word):
                print("Congratulations, You won!")
                print(f"The word is: {word}")
                break
        else:
            # If out of chances
            print('You lost! Try again..')
            print(f'The word was: {word}')

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
