import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word, INITIAL_GUESSES):
    print("")
    true_answer= secret_word #The chosen word stored as a variable
    length_of_answer = "-" * len(true_answer)
    print ("The word looks like:", length_of_answer)
    print ("")
    guessed_letters = [] #A list that will append the users correct inputs as the game goes on
    true_answer_list = [] #A variable that will store the list version of the chosen word for the game
    true_answer_list_placeholder = list(true_answer)
    for i in true_answer_list_placeholder: #Needed to create a loop that will add the characters of the chosen word into the list variable removing duplicates
        if i not in true_answer_list:
            true_answer_list.append(i)
    while INITIAL_GUESSES > 0:
        guess = input("Please type a single letter here, then press the enter key: ").upper()
        print("")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. \n")
            elif guess in true_answer_list:
                print("Nice job!", guess, "is in the word! \n")
                guessed_letters.append(guess)
                print ("The word now looks like: " )
                if guess in true_answer:
                    """
                    index = [i for i, l in enumerate(true_answer) if l == guess] #1st way start
                    for i in index:
                        #length_of_answer = length_of_answer[:i] + guess + length_of_answer[i+1:] #1st way end  
                    index = [] #2nd way start
                    for i, letter in enumerate(true_answer):
                        if letter == guess:
                            index.append(i)             
                            for i in index:
                                length_of_answer = length_of_answer[:i] + guess + length_of_answer[i+1:]#2nd way end
                print(length_of_answer)
                """
                for i, letter in enumerate(true_answer): #3rd way start
                    if guess == true_answer:
                        length_of_answer[i] = guess
                print ("".join(length_of_answer)) #3rd way end
            elif guess not in true_answer:
                print ("That letter is not in the word \n")
                INITIAL_GUESSES -= 1
                print ("You have ", INITIAL_GUESSES, " guesses remaining.")
            if sorted(guessed_letters) == sorted(true_answer_list):
                break
        else:
            print ("Sorry that is not a valid guess!")
    if INITIAL_GUESSES == 0:
        print ("Unfortunately you were unable to guess the word. It was", true_answer)
    else:
        print ("Congratulations! You were able to correctly guess the word!", true_answer)


def get_word(): #two versions of get_word one to extract from a file of words or one with a limited selection
    
    with open("Lexicon.txt") as lexicon: #open file function that will return a randomly selected word from a text document
        word_selection = lexicon.read()
        word_selection = word_selection.split()
        word_selected = (random.choice(word_selection))
    return word_selected.upper()
    """
    random_index = random.randint(1,4)
    if random_index == 1:
        return "GOOD"
    if random_index == 2:
        return "PYTHON"
    if random_index == 3:
        return "COMPUTER"
    if random_index == 4:
        return "HAPPY"
    """


def play_again(): #A function that allows the user to play again
    play_again = input("Would you like to play again? (Y/N) \n").upper()
    while play_again != "N" :
        if play_again == "Y":
            secret_word = get_word()
            play_game(secret_word, INITIAL_GUESSES)
            play_again = input("Would you like to play again? (Y/N) \n").upper()
        elif play_again == "N":
            break
        elif play_again != "Y" or "N": #If the user does not type Y or N the input will loop until a valid entry
            print ("That is an invalid input. Please respond with Y or N. \n")
            play_again = input("Would you like to play again? (Y/N) \n").upper()
    print ("Thanks for playing! :)")


def main():
    print("Welcome to 'WordGuess with Python' as the user you will have", INITIAL_GUESSES, "chances to guess the mystery word! \n An incorrect guess will consume one of your guesses, but a correct guess will not. \n Good luck and have fun!")
    secret_word = get_word()
    play_game(secret_word, INITIAL_GUESSES)
    play_again()
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
