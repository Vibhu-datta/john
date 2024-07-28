

def show_letter(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print("\n")



# show image
# show the word 

def hangman():
    word='tree'
    wrong_guesses=0
    guessed_letters = []
    while wrong_guesses < 6:
    # ask user to guess letter
        user_input= input("Guess Letter:")
        # check if letter is apart of word
        if user_input in word:
            guessed_letters.append(user_input)
        else:
            wrong_guesses=wrong_guesses+1
        show_letter(word, guessed_letters)
    print("you lose")

hangman()
    # if in word add letter 
    # if not add body partb
    # repeat process 


# if word not guessed before person complete 
# if lose show word
# if win show win screen
#


