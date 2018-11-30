import Hangman.HangmanGame


print("****************")
print("1] Hangman")
print("2] Exit")
print("****************")

choice = input("\nEnter your choice:")

if choice == "1":
    Hangman.HangmanGame.hangman_func()
else:
    print("Goodbye!")
    exit()


