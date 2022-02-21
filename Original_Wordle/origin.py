file = open("./words1.txt", "r")
wordleWords = open("wordleWords.txt", "a")
# print(file.read(2))

import string

count = 0
words = []
for line in file:
    if str(line)[:-1] == "HelloWorld":
        print("hello", line)
    if count == 1807: 
        print(count ,line)

    if count == 1809:
        print(line)
        line = str(line)
        word = ""
        for letter in line:
            if letter in string.ascii_letters:
                word += letter
            elif letter == ",":
                wordleWords.write(word + "\n")
                word = ""
        wordleWords.write(word + "\n")

    # line = str(line)
    # word = line[1:-3]
    # wordleWords.write(word + "\n")

    if count == 1820:
        break
    
    count += 1

    # # print(line)
    # count += 1
    # word = str(line)
    # print(word)
    # for letter in word:
    #     print(letter)
    #     if letter == "\n":
    #         count = 10
    #         break

    # word = word[1:-3]

    # words.append(word)
    # if count == 10:
    #     break
# print(words)