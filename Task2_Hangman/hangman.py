import random

# Word list
words = ["python", "developer", "internship", "programming", "github"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game")
print("Guess the word")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You won the game!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)
    else:
        print("✅ Good guess!")

if attempts == 0:
    print("😢 You lost! The word was:", word)
