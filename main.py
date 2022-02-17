# Author: Alexander Sutter
# Date: 2/16/22
# Last Modified: 2/17/22

from datetime import date

def openLogFile(fileName="fileReadingWriting_Base_Default.txt"):
  try:
    return open(fileName, "a")
  except:
    print("error opening file")

def writeLog(logItem):
  logFile = openLogFile("wordleLog.txt")
  logFile.write(logItem + "\n")
  logFile.close()

def log(logItem):
  # print("log item: " +str(logItem))
  writeLog("log item: " +str(logItem))

def logError(logItem):
  # print("Error: " +str(logItem))
  writeLog("Error: " +str(logItem))

# returns current date as yyyy-mm-dd (2022-02-17)
def getCurrentDate():
  today = date.today()
  return today

def main():
  print("Hello World")
  log("Hello World")
  print(getCurrentDate())

main()