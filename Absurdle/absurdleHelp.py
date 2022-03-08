#Author: Alexander Sutter
#Date: 3/7/2022
#Last Revision: 3/7/2022

def green(letter, i, words):
    removedWords = []
    
    newremovedWords = ["",""]
    while(len(newremovedWords) != 0):
        newremovedWords = []
        for word in words:
            if word[i] != letter:
                removedWords.append(word[:-1])
                newremovedWords.append(word[:-1])
                words.remove(word)
    print(letter, i, removedWords, words)
    return words
        
def yellow(letter, i, words):
    removedWords = []
    
    newremovedWords = ["",""]
    while(len(newremovedWords) != 0):
        newremovedWords = []
        for word in words:
            if word[i] == letter:
                removedWords.append(word[:-1])
                newremovedWords.append(word[:-1])
                words.remove(word)
            if letter not in word:
                removedWords.append(word[:-1])
                newremovedWords.append(word[:-1])
                words.remove(word)
    print(letter, i, removedWords, words)
    return words

def gray(letter, words):
    removedWords = []
    
    newremovedWords = ["",""]
    while(len(newremovedWords) != 0):
        newremovedWords = []
        for word in words:
            if letter in word:
                print(letter, word)
                removedWords.append(word[:-1])
                newremovedWords.append(word[:-1])
                words.remove(word)
        print(letter, len(newremovedWords), newremovedWords, len(words), "\n\n", words)
    print(letter, len(removedWords), removedWords, len(words), "\n\n", words)
    return words

def main():
    file = open("words.txt", "r")
    
    words = []
    for line in file:
        words.append(str(line))
    
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
                break
        
        print("\n\n\n<----------Possible Words are ----------->" + str(len(words)))
        print(words)
        print(word)

main()