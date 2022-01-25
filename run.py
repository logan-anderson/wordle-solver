
from random import random
import string


f = open('wordList.txt')
words = f.read().lower().splitlines()
lettersIn = []
lettersNotIn = []
lettersInPos = []


# Filter letters that only have the right letters with the right pos
def filterLettersInPos(word: string):
    if len(lettersInPos) == 0:
        return True
    returnVal = True
    for (pos, letter) in lettersInPos:
        if word[pos] != letter:
            returnVal = False
    return returnVal

# Filter out letters that are not in the word


def filterLettersNotIn(word: string):
    if len(lettersNotIn) == 0:
        return True
    for letter in word:
        if letter in lettersNotIn:
            return False
    return True

# Filter out letters that are in the word


def filterLeters(word: string):
    if len(lettersIn) == 0:
        return True
    for letter in word:
        if letter in lettersIn:
            return True

    return False


def pickWord():
    filterTwice = list(filter(
        filterLettersNotIn, words))
    filterOnce = list(filter(
        filterLeters, filterTwice))

    newWords = list(filter(filterLettersInPos, filterOnce))

    if len(newWords) == 0:
        print("ERROR: no more words")
        exit(1)

    pick = int(random()*len(newWords)) - 1
    return newWords[pick]


done = False
while not done:
    word = pickWord()
    print(word)
    print('Enter letters that are not in the word (seperated by comma)')
    for x in input().split(','):
        if x:
            lettersNotIn.append(x.strip().lower())

    print('Enter letters that are in the word (seperated by comma)')
    for x in input().split(','):
        if x:
            lettersIn.append(x.strip().lower())
    print('Enter letters and position that are in the word (seperated by comma)')
    for x in input().split(','):
        if x:
            ents = x.split("|")
            lettersInPos.append((int(ents[0]), ents[1].strip().lower()))
    print('Are you done?')
    done = input() == 'yes'


f.close()
