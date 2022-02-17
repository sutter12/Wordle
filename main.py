# Author: Alexander Sutter
# Date: 2/16/22
# Last Modified: 2/17/22

from datetime import date

def openFile(fileName="fileReadingWriting_Base_Default.txt"):
  try:
    return open(fileName, "a")
  except:
    print("error opening file")

def writeFile(fileName, data, completeLine = True):
  file = openFile(fileName)
  if completeLine:
    file.write(data + "\n")
  else: 
    file.write(data)
  file.close()

def log(logItem, error = False):
  # print("log item: " +str(logItem))
  if not error: # for all normal log items
    writeFile("wordleLog.txt", "log item: " +str(logItem), True)
  else: # for errors
    writeFile("wordleLog.txt", logItem, True)

def logError(logItem):
  # print("Error: " +str(logItem))
  log("Error: " +str(logItem), True)

def writeWordHistory():
  today = str(getCurrentDate())
  word = "Test"

  #format: 2022-02-16,caulk
  line = today + "," + word

  writeFile("wordHistory.csv", line)
  log("wordHistory.csv written with: " + line)

def writeUserHistory(tries, guesses, word = "Test,"):
  today = str(getCurrentDate()) + ","
  tries = str(tries) + ","

  #format: 2022-02-16,caulk,5,trash,pylon,weird,laugh,caulk,-
  line = today + word + tries
  for guess in guesses:
    line += guess + ","

  writeFile("userHistory.csv", line)
  log("userHistory.csv written with: " + line)

def getCurrentDate():
  # returns current date as yyyy-mm-dd (2022-02-17)
  today = date.today()
  log("date request; current date: " + str(today) + ";")
  return today

def main():
  log("Start Program;")
  # writeWordHistory()
  # guesses = ["trash", "pylon", "weird", "laugh", "caulk", "-"]
  # writeUserHistory(5, guesses)

main()