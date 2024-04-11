"""
Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and 
inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts 
the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits.
Otherwise, the program prints the line associated with that number.9
""" 

# Prompt File Name & Open File
fileName = input("Please enter File Name: ")
file = open(fileName)

# Pass Lines of text into a list
lines = file.readlines()

# Prompt user for a line number (1 and above, 0 to quit)
while True:
    print("Total Number of Lines in Text file: ", len(lines))
    lineNum = input("Please enter a line number: ")
    if lineNum == 0:
        break
    lineNum = int(lineNum) - 1
    print(lines[lineNum])
