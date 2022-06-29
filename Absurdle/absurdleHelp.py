#Author: Alexander Sutter
#Date: 3/7/2022
#Last Revision: 3/7/2022

def green(letter, i, words):
    goodWords = []
    
    for word in words:
        if word[i] == letter:
            goodWords.append(word)
    # print(letter, i, len(goodWords), goodWords)
    return goodWords
        
def yellow(letter, i, words):
    goodWords = []
    
    for word in words:
        if letter in word and word[i] != letter:
            goodWords.append(word)
    # print(letter, i, len(goodWords), goodWords)
    return goodWords

def gray(letter, words):
    goodWords = []
    
    for word in words:
        if letter not in word:
            # print(letter, word)
            goodWords.append(word)
    # print(letter, len(goodWords), goodWords, "\n\n")
    return goodWords

# def correctColor(guess, colors):
#     repeatLetters = []
#     repeatLetter = ''
#     for letter in guess:
#         if letter not in repeatLetters:
#             repeatLetters.append(letter)
#         else:
#             repeatLetter = letter
#     return colors

def repeatLetter(guess, colors):
    return colors

def getWordsList(filename):
    file = open(filename, "r")
    
    words = []
    for line in file:
        word = str(line)
        # if word[5:] ==  '\n':
        #     word = word[:-1] 
        word = word[0:5]   
        words.append(word)
    
    return words

def main():
    words = getWordsList("words.txt")
    
    print(words)
    
    badLetters = ""
    word = ["", "", "", "", ""]
    
    incorrect = True
    while(incorrect):
        # get users guess and check it 
        userGuess = ""
        while(len(userGuess) != 5):
            userGuess = input("What was your guess: ")
        
        # get colors of users guess and check it
        colors = ""
        while(len(colors) != 5):
            colors = input("What are the colors (g->green, y->yellow, b->black/gray): \n" + userGuess + "\n")
            if colors == 'all':
                incorrect = False
                print("Word is: " + userGuess)
                break
        
        # color = correctColor(userGuess, colors) #fixes issue with having multiple of the same letter in a guess #bobbby

        # narrow down remaining possible words
        if incorrect: # code not run if user guessed word   
            for i in range(5):
                letter = userGuess[i]

                if i<4:
                    restOfWord = userGuess[(i+1):]
                    print(restOfWord)
                    if letter in restOfWord:
                        colors = repeatLetter(userGuess, colors)

                color = colors[i]

                if color == "g":
                    word[i] = letter
                    words = green(letter, i, words)
                elif color == "y":
                    words = yellow(letter, i, words)
                elif color == "b":
                    badLetters += letter
                    words = gray(letter, words)
            
            print("\n\n\n<----------Possible Words are -----------> ")
            print("["+str(len(words))+"] = ", end='')
            print(words)
            print(word)

main()