f = open('wordList.txt')
words = f.read().lower().splitlines()
letters = {}
for word in words:
    for letter in word:
        if not letters.get(letter):
            letters[letter] = 1
        else:
            letters[letter] = letters[letter] + 1

print(letters)

f.close()
