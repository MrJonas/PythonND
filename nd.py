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
