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


# Funtion to to write sorted dict to stats file:
def dict_print(file_dict, sum_dict):
    for key in sorted(file_dict, key=file_dict.get, reverse=True):
        if str(key) == " ":
            stats_file.write(str(file_dict[key]) + ' Space\n')
        elif str(key) == "\n":
            stats_file.write(str(file_dict[key]) + ' New Line\n')
        else:
            stats_file.write(str(file_dict[key]) + ' ' + str(key) + "\n")
        sum_dict[key] = sum_dict.get(key, 0) + file_dict[key]
    return sum_dict
# Creates stats file in specified directory:
stats_file_path = str(directory_path) + str('Directory_Statistics.txt')
stats_file = open(stats_file_path, 'w+')
# Reads all files in specified directory:
symbols = {}
words = {}
sum_symbols = {}
sum_words = {}
for data in os.listdir(directory_path):
    file_path = str(directory_path) + str(data)
    if os.path.isfile(file_path) and file_path != stats_file_path:
        read_file = open(file_path, 'r')
        text = read_file.read()
        read_file.close()
        symbols = count_symbols(text)
        words = count_words(text)
        stats_file.write('File:\n' + str(file_path) + '\nWords statistics:\n')
        sum_words = dict_print(words, sum_words)
        stats_file.write('File:\n' + str(file_path))
        stats_file.write('\nSymbols statistics:\n')
        sum_symbols = dict_print(symbols, sum_symbols)
# Prints directory statistics
stats_file.write('Directory:\n' + str(directory_path))
stats_file.write('\nWords statistics:\n')
sum_words = dict_print(sum_words, sum_words)
stats_file.write('Directory:\n' + str(directory_path))
stats_file.write('\nSymbols statistics:\n')
sum_symbols = dict_print(sum_symbols, sum_symbols)
# Closes stats file:
stats_file.close()
