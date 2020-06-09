import random

languages = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(languages)
letters = list(word)
cover = list("-" * len(word))
lives = 8
guesses = []

def hangman():
    global letters
    global lives
    global guesses
    global cover

    while lives >= 0:
        if cover == letters:
            print("You guessed the word!")
            print("You survived!")
            break

        if lives == 0:
            print("You are hanged!")
            break

        print()
        print("".join(cover))

        guess = input("Input a letter:")

        if len(guess) != 1:
            print("You should input a single letter")

        elif guess.islower() is False or guess.isalpha() is False:
            print("It is not an ASCII lowercase letter ")

        elif guess in guesses:
            print("You already typed this letter")

        elif guess in letters:
            for x in range(0, len(cover)):
                if guess == letters[x]:
                    cover[x] = guess

        elif guess not in letters:
            lives -= 1
            print("No such letter in the word")

        if len(guess) == 1:
            guesses.append(guess)


print("H A N G M A N")  # Write your code here
start = input('Type "play" to play the game, "exit" to quit:')
if start == "play":
    hangman()



