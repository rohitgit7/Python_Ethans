import random


def hangman_func():
    fo = open("Hangman\\file.txt", "r+")
    file_list = fo.read().split()

    random_word = random.sample(file_list, 1)
    print(random_word)
    guess = 3
    counter = 0
    list_random_word = list(random_word[0])

    name = input("What is your name:")
    print("Hello %s, lets play Hangman!" % name)
    print("\nStart guessing...")

    lt = ['_' for i in range(len(list_random_word))]    # create a list of '_'
    print(' '.join(x for x in lt))                      # join the list to show all characters in list as string

    while guess > 0 and counter < len(list_random_word):
        read = input("Guess a character:")
        if read == list_random_word[counter]:
            lt[counter] = read
            print(' '.join(x for x in lt))
            counter += 1
        else:
            guess -= 1
            print("Wrong!")
            print("You have %d more guesses" % guess)
            print(' '.join(x for x in lt))
    if guess > 0 and counter == len(list_random_word):
        print("You won! Yayyy!!")
    else:
        print("You are out of no. of guesses. You lost!")
        print("Game over!")
    fo.close()


if __name__ == "__main__":
    hangman_func()
