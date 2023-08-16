"""You will write three functions for this exercise. First, write a writeToFile() function with two parameters for the filename 
of the file and the text to write into the file. Second, write an appendToFile() function, which is identical to writeToFile() 
except that the file opens in append mode instead of write mode. Finally, write a readFromFile() function with one parameter for 
the filename to open. This function returns the full text contents of the file as a string.

These Python instructions should generate the file and the assert statement checks that the content is correct:

writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

This code writes the text 'Hello!\n' and 'Goodbye!\n' to a file named greet.txt, then reads in this file’s content to verify it is correct. 
You can delete the greet.txt file after running these instructions program.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: text file reading and writing"""

def writeToFile(file_name, word):
    with open(file_name, 'w') as file:
        file.write(word)

def appendToFile(file_name, word):
    with open(file_name, 'a') as file:
        file.write(word)

def readFromFile(file_name):
    with open(file_name, 'r') as file:
        return file.read()

writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

