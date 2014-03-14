#! /usr/bin/env python
#! coding: utf:-8
import sys
import os
# Checks if entered directory path exist:
if len(sys.argv) < 2:
    print("Enter directory path")
    quit()
elif not os.path.isdir(sys.argv[1]):
    print("Entered directory does not exists")
    quit()
else:
    directory_path = sys.argv[1]
# Temponary text file:
text_path = "/home/jonas/progr/1.txt"
f = open(text_path, 'r')
text = f.read()
f.close
print(text)


# Function for counting symbols:
def count_symbols(text):
    symbols = {}
    for i in range(len(text)):
        if text[i] in symbols:
            symbols[text[i]] = symbols[text[i]] + 1
        else:
            symbols[text[i]] = 1
    return symbols
# Temponary printing counted symbols
p = count_symbols(text)
print(p)
for i in sorted(p, key=p.get, reverse=True):
    print(str(p[i]) + str(i))


# Function for counting words:
def count_words(text):
    new_word = ""
    words = {}
    for i in range(len(text)):
        if text[i] in (' \n\'\".,?!()[]{}'):
            if str(new_word) in  words and new_word != "":
                words[str(new_word)] = words[str(new_word)] + 1
            elif new_word != "":
                words[str(new_word)] = 1
            new_word = ""
        else:
            new_word = str(new_word) + str(text[i])
    return words
# Temponary printing:
w = count_words(text)
for i in sorted(w, key=w.get, reverse=True):
    print(str(w[i]) + str(i))
