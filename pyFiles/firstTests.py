#! python3

# Importing date class from datetime module
import datetime
from genericpath import isfile
from multiprocessing.connection import wait
from posixpath import split
today = datetime.datetime.now() # Gets today date
day = today.strftime("%Y") # YYYY
month = today.strftime("%m") # MM
year = today.strftime("%d") # DD
weekday = today.strftime("%A") # Weekday
time = today.strftime("%X") # HH:MM:SS
date = "{0}/{1}/{2} {3}".format(day,month,year,weekday)
print(date)
print(time.center(len(date), "-"))

# Importing copy and paste from/to computer
import pyperclip
pyperclip.copy("https://chrisngdc.github.io/") # Copy to clipboard
pasted = pyperclip.paste() # Paste from clipboard
print(pasted) # Should print "https://chrisngdc.github.io/"

# Importing copy of mutable objets
import copy
original = ["A","B","C","D"]
simpleCopy = original
AdvanceCopy = copy.deepcopy(original)
original.append("E")
print("Original:",original)
print("Simple Copy:",simpleCopy)
print("Advance Copy:",AdvanceCopy)

# Importing pprint (pretty print) for better dictionary print
import pprint

# Importing Sys (System)
import sys
variables = sys.argv # System variables given on the command line
del variables[:1] # Delete the first element because it's the path of the .py
print(variables)

# # Programm
# def get(question, condition, errorText):
#     while True:
#         print(question)
#         getInput = input()
#         try:
#             if condition(getInput):
#                 return getInput
#             else:
#                 print(errorText)
#         except ValueError:
#             print(errorText)
# print("Hello")
# name = get("What is your name?",lambda a : a != "","Please type your name!")
# print("It's a pleasure to meet you " + name)
# print("The length of your name is:", len(name))
# age = int(get("What is your age?",lambda a : int(a) > 0,"Please type a valid age!"))
# offset = get("Has your birthday already passed? (Y/N)",lambda a : a.upper() == "Y" or a.upper() == "N","Please type Y or N!").upper()
# if offset == "N" :
#     age += 1
# print("You were born in", (today.year - age))

# # Character Count
# message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi venenatis."
# count = {} # "r" : 5

# for c in message.upper():
#     count.setdefault(c, 0)
#     count[c] += 1

# pprint.pprint(count)

# Files y folders manipulation
import os, shutil

totalSize = 0
folderPath = "C:\Windows\Cursors"
for fileName in os.listdir(folderPath):
    filePath = os.path.join(folderPath, fileName)
    if os.path.isfile(filePath):
        totalSize += os.path.getsize(filePath)
print(totalSize)

if not os.path.exists(".//pyFiles//images"):
    print("No esiste, creando")
    os.makedirs(".//pyFiles//images") # Creates folders necesaries
    f = open(".//pyFiles//images//prueba.txt", "xt") # Creates the file
    shutil.copy(".//pyFiles//images//prueba.txt",".//pyFiles//images//pruebaBackup.txt") # Copy the file
    shutil.rmtree(".//pyFiles//imagesBackup")
else:
    print("Existe, borrando")
    shutil.copytree(".//pyFiles//images",".//pyFiles//imagesBackup") # Copy the entire folder
    shutil.rmtree(".//pyFiles//images") # Removes folders