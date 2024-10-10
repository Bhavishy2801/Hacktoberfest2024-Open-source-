import random

# List of words to guess from
word_list = ['python', 'hangman', 'coding', 'programming', 'algorithm', 'data', 'science']

# Function to get a random word
def get_random_word():
    return random.choice(word_list)

# Function to display the current guessed state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Main game function
def hangman():
    word = get_random_word()
    guessed_letters = []
    tries = 6  # Number of incorrect guesses allowed
    guessed = False

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("_ " * len(word))

    while not guessed and tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good guess! '{guess}' is in the word.")
                guessed_letters.append(guess)

            current_display = display_word(word, guessed_letters)
            print(current_display)

            if "_" not in current_display:
                guessed = True
        else:
            print("Invalid input. Please guess a single letter.")

        print(f"You have {tries} tries left.")

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

# Start the game
hangman()
