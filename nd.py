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


# Function for counting symbols:
def count_symbols(text):
    symbols = {}
    for i in range(len(text)):
        if text[i] in symbols:
            symbols[text[i]] = symbols[text[i]] + 1
        else:
            symbols[text[i]] = 1
    return symbols


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
# Creates stats file in specified directory:
stats_file_path = str(directory_path) + str('Directory_Statistics.txt')
stats_file = open(stats_file_path, 'w+')
# Reads all files in specified directory:
for data in os.listdir(directory_path):
    file_path = str(directory_path) + str(data)
    if os.path.isfile(file_path):
        read_file = open(file_path, 'r')
        text = read_file.read()
        read_file.close()
        print(text)
# Closes stats file:
stats_file.close()
