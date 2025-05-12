# print("     ___________     \n    |           |    \n    |           O    \n    |          /|\\  \n    |          / \\  \n    |                \n    |                \n_________            ")
# print("    |           |    ")
# print("    |           O    ")
# print("    |          /|\\  ")
# print("    |          / \\  ")
# print("    |                ")
# print("    |                ")
# print("    |                ")
# print("_________            ")


def hangman(count):
    sketch1 = "     ___________     \n    |           |    \n    |                \n    |               \n    |               \n    |                \n    |                \n_________            "
    sketch2 = "     ___________     \n    |           |    \n    |           O    \n    |               \n    |               \n    |                \n    |                \n_________            "
    sketch3 = "     ___________     \n    |           |    \n    |           O    \n    |           |   \n    |               \n    |                \n    |                \n_________            "
    sketch4 = "     ___________     \n    |           |    \n    |           O    \n    |          /|   \n    |               \n    |                \n    |                \n_________            "
    sketch5 = "     ___________     \n    |           |    \n    |           O    \n    |          /|\\  \n    |               \n    |                \n    |                \n_________            "
    sketch6 = "     ___________     \n    |           |    \n    |           O    \n    |          /|\\  \n    |          /    \n    |                \n    |                \n_________            "
    sketch7 = "     ___________     \n    |           |    \n    |           O    \n    |          /|\\  \n    |          / \\  \n    |                \n    |                \n_________            "
    sketches =[sketch1, sketch2, sketch3, sketch4, sketch5, sketch6, sketch7]
    for i in range(7):
        if count == i:
            print(sketches[i])

def setStage(stage):
    for x in stage:
        print(x, end=" ")
    print()

def setAlphabets(alphabets):
    for y in alphabets:
        print(y, end=" ")
    print()

def playGame(word):
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    length = len(word)
    stage = ["_ " for _ in range(length)]
    stageWord = word.copy()
    count = 0
    while word != []:
        hangman(count)
        setAlphabets(alphabets)
        setStage(stage)
        letter = input("Choose a letter: ").upper()
        if letter in alphabets:
            if letter in word:
                ind = stageWord.index(letter)
                stage[ind] = letter
                word.remove(letter)
                if letter not in word:
                    alphabets.remove(letter)
            else:
                count += 1
                if count > 6:
                    print("You lose!")
                    return
        else:
            print("----------------------------------------")
            print("Not valid. Choose from remaining letters")
            print("----------------------------------------")
    print(f"You win! The word was {"".join(stage)}!")


word = list("BINOCULARS")

playGame(word)






