"""
Author: Joseph Fleming, flemin53@purdue.edu
Assignment: mm.n - Solo Wof
Date: 12/2/2021

Description:
    This program, using custom functions, nested loops, boolean evaluators,
    random numbers, imported modules, printing formatting, string concatenation,
    list analysis, inputting text files, and a bit of spit-shine old fashioned elbow-grease,
    runs a solo game of wheel of fortune precisely to the specifications of the assignment!

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

# Import modules below this line (starting with unit 6).
import random

# Write new functions below this line (starting with unit 4).
def load_phrases():
    with open("phrases.txt", "r") as file:
        transcript = file.read()
    phrases = transcript.split("\n")
    while "" in phrases:
        phrases.remove("")
    random.shuffle(phrases)
    return phrases

def spin_the_wheel():
    spaces = [
    500,
    500,
    500,
    500,
    550,
    550,
    600,
    600,
    600,
    600,
    650,
    650,
    650,
    700,
    700,
    800,
    800,
    900,
    2500,
    "BANKRUPT",
    "BANKRUPT"
    ]
    space = spaces[random.randint(0,len(spaces)-1)]
    return space

def string_to_list(string):
    letters = []
    for letter in string:
        letters.append(letter)
    return letters

def get_letter_position(letter, list_of_letters):
    letter_positions = []
    for position in range(0,len(list_of_letters)):
        if list_of_letters[position] == letter:
            letter_positions.append(position)
    return letter_positions

def main():
    print("Welcome to Solo Wheel of Fortune!")
    print()
    playing = True
    n = 0
    doVowelReplace = False
    doConsonantReplace = False
    bank = 0
    allPhrases = load_phrases()
    for n in range(0,4):
        #beginning of round!
        earnings = 0
        currentPhrase = allPhrases[n]
        blankCurrentPhrase = currentPhrase.upper()
        unusedConsonants = "bcdfghjklmnpqrstvwxyz".upper()
        unboughtVowels = "AEIOU"
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            blankCurrentPhrase = blankCurrentPhrase.replace(letter,"_")
        wallet = 0.0
        guessing = False
        quitting = False
        #playing the round
        while True:
            #Show menu
            doVowelReplace = False
            doConsonantReplace = False
            print(f":: Solo WoF :::::::::::::::::::::::::::::: Round {n+1} of 4 ::")
            print("::", end="")
            print(blankCurrentPhrase.center(54),end="")
            print("::")
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("::   "+unboughtVowels+"   ::   "+unusedConsonants+"   ::",end="")
            print(("${:,.0f}".format(wallet)).rjust(11),end=" ::\n")
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            while True:
                print()
                print("Menu:")
                print("  1 - Spin the wheel.")
                print("  2 - Buy a vowel.")
                print("  3 - Solve the puzzle.")
                print("  4 - Quit the game.")
                print()
            #Handle choices
                choice = input("Enter the number of your choice: ")
                if choice == "1":
                    if unusedConsonants == "                     ":
                        print("There are no more consonants to choose.")
                        break
                    space = spin_the_wheel()
                    if space != "BANKRUPT":
                        print(f"The wheel landed on ${space:,.0f}.")
                        while True: #Handle invalid choices
                            letterChoice = input("Pick a consonant: ")
                            if len(letterChoice) > 1 or letterChoice == "":
                                print("Please enter exactly one character.")
                            elif letterChoice.lower() in "aeiou":
                                print("Vowels must be purchased.")
                            elif letterChoice.lower().isalpha() != True:
                                print(f"The character {str(letterChoice)} is not a letter.")
                            elif letterChoice.upper() not in unusedConsonants:
                                print(f"The letter {letterChoice.upper()} has already been used.")
                            elif letterChoice.lower().isalpha():
                                unusedConsonants = unusedConsonants.replace(letterChoice.upper(), " ")
                                if letterChoice.upper() in currentPhrase or letterChoice.lower() in currentPhrase:
                                    doConsonantReplace = True #Flag to do letter replacements at the end of round
                                    break #leave loop that forces consonants to be valid
                                else:
                                    print(f"I\'m sorry, there are no {letterChoice.upper()}\'s.")
                                    break #leave loop that forces consonants to be valid
                            else:
                                print("Encountered a strange exception. try again please!")
                        break #leave "show menu" loop and go to next stage of round
                    else:
                        print("The wheel landed on BANKRUPT.") #Does not run above code at all, and empties wallet
                        print(f"You lost ${wallet:,.0f}!")
                        wallet = 0.0
                        break


                elif choice == "2":
                    if unboughtVowels == "     ":
                        print("There are no more vowels to buy.")
                        break
                    if wallet > 275:
                        while True:
                            letterChoice = input("Pick a vowel: ") #Handles invalid vowel choices
                            if len(letterChoice) != 1 or letterChoice == "":
                                print("Please enter exactly one character.")
                            elif letterChoice.lower().isalpha() != True:
                                print(f"The character {str(letterChoice)} is not a letter.")
                            elif letterChoice.lower() not in "aeiou":
                                print("Consonants cannot be purchased.")
                            elif letterChoice.upper() not in unboughtVowels:
                                print(f"The letter {letterChoice.upper()} has already been purchased.")
                            elif letterChoice.lower() in "aeiou":
                                unboughtVowels = unboughtVowels.replace(letterChoice.upper(), " ")
                                if letterChoice.upper() in currentPhrase or letterChoice.lower() in currentPhrase:
                                    doVowelReplace = True #Flag to do letter replacement at end of round
                                else:
                                    print(f"I\'m sorry, there are no {letterChoice.upper()}\'s.") #Does not set the flag, and continues
                                wallet -= 275
                                break #leaves invalid choice loop
                        break #leaves "show menu" loop
                    else:
                        print("You need at least $275 to buy a vowel.") #bypassed entirely
                        break #leaves "show menu" loop
                elif choice == "3":
                    guessing = True
                    print("Enter your solution.")
                    print("  Clues: " + blankCurrentPhrase)
                    guess = input("  Guess: ")
                    if guess.upper() == currentPhrase.upper():
                        correctGuess = True
                    else:
                        correctGuess = False
                    break #go to end of round with specified state

                elif choice == "4":
                    guessing = True
                    correctGuess = None
                    quitting = True
                    earnings = 0
                    break #go to end of round

                else:
                    print(f"\"{choice}.\" is an invalid choice.")
                    continue


            #Begin end of round stages
            #Letter replacements
            if doVowelReplace:
                currentPhraseLettersList = string_to_list(currentPhrase)
                if (currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower()))) == 1:
                    print(f"There is {(currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower())))} {letterChoice.upper()}.")
                elif (currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower()))) >=1:
                    print(f"There are {(currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower())))} {letterChoice.upper()}\'s.")
                else:
                    print("something has been evaluated incorrectly")
                indicesToReplace = get_letter_position(letterChoice.upper(),currentPhraseLettersList)
                indicesToReplace += get_letter_position(letterChoice.lower(),currentPhraseLettersList)
                blankCurrentPhraseLettersList = string_to_list(blankCurrentPhrase)
                for index in indicesToReplace:
                    blankCurrentPhraseLettersList[index] = currentPhraseLettersList[index].upper()
                blankCurrentPhrase = "".join(blankCurrentPhraseLettersList) #works by making the current phrase and the blank current phrase into lists, seeing which letters are the same as your letter choice, and updating blank current phrase

            if doConsonantReplace:
                currentPhraseLettersList = string_to_list(currentPhrase)
                if (currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower()))) == 1:
                    print(f"There is 1 {letterChoice.upper()}, which earns you ${space:,.0f}.")
                elif (currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower()))) >= 1:
                    print(f"There are {(currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower())))} {letterChoice.upper()}\'s, which earns you ${(space*(currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower())))):,.0f}.")
                else:
                    print("something has been evaluated incorrectly")
                wallet += space*(currentPhraseLettersList.count(letterChoice.upper())+(currentPhraseLettersList.count(letterChoice.lower())))
                indicesToReplace = get_letter_position(letterChoice.upper(),currentPhraseLettersList)
                indicesToReplace += get_letter_position(letterChoice.lower(),currentPhraseLettersList)
                blankCurrentPhraseLettersList = string_to_list(blankCurrentPhrase)
                for index in indicesToReplace:
                    blankCurrentPhraseLettersList[index] = currentPhraseLettersList[index].upper()
                blankCurrentPhrase = "".join(blankCurrentPhraseLettersList)

            #Guess phrase
            if guessing: #if you have guessed the phrase
                break #exit round loop
            print()
        #End of round!
        if type(correctGuess) == None:
            earnings = 0
            quitting = True
            break #go to end of game
        elif correctGuess == True:
            print("Ladies and gentlemen, we have a winner!")
            if wallet < 1000:
                wallet = 1000
            bank += wallet
            earnings = wallet
        elif correctGuess == False:
            print("I\'m sorry. The correct solution was:")
            print(currentPhrase.upper())
            earnings = 0
        wallet = 0
        print()
        print(f"You earned ${earnings:,.0f} this round.")
        print()
        if quitting:
            break #exit game loop. game loop automatically ends after 4 rounds

    print(f"Thanks for playing!\nYou earned a total of ${bank:,.0f}.")

if __name__ == '__main__':
    main()
