#Author: Alexander Sutter
#Date: 3/7/2022
#Last Revision: 3/7/2022

def green(letter, i, words):
    goodWords = []
    
    for word in words:
        if word[i] == letter:
            goodWords.append(word)
    print(letter, i, len(goodWords), goodWords)
    return goodWords
        
def yellow(letter, i, words):
    goodWords = []
    
    for word in words:
        if letter in word and word[i] != letter:
            goodWords.append(word)
    print(letter, i, len(goodWords), goodWords)
    return goodWords

def gray(letter, words):
    goodWords = []
    
    for word in words:
        if letter not in word:
            print(letter, word)
            goodWords.append(word)
    print(letter, len(goodWords), goodWords, "\n\n")
    return goodWords

def getWordsList(filename):
    file = open(filename, "r")
    
    words = []
    for line in file:
        word = str(line)
        if word[5:] ==  '\n':
            word = word[:-1]    
        words.append(word)
    
    return words

def main():
    words = getWordsList("words.txt")
    
    print(words)
    
    badLetters = ""
    word = ["", "", "", "", ""]
    
    incorrect = True
    while(incorrect):
        userGuess = ""
        while(len(userGuess) != 5):
            userGuess = input("What was your guess: ")
        
        for i in range(5):
            letter = userGuess[i]
            color = input("What was " + letter + "'s color: ")

            if color == "ge":
                word[i] = letter
                words = green(letter, i, words)
            elif color == "y":
                words = yellow(letter, i, words)
            elif color == "ga":
                badLetters += letter
                words = gray(letter, words)
            elif color == "all":
                incorrect = False
                print("Word is: " + userGuess)
                break
        
        print("\n\n\n<----------Possible Words are ----------->" + str(len(words)))
        print(words)
        print(word)

main()