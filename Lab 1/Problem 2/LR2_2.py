"""
Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and 
inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts 
the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits.
Otherwise, the program prints the line associated with that number.9
""" 
import os

def main():
    fileFound = False
    
    # Prompt for filename
    while not fileFound:
        filename = input("Enter the filename (including path if necessary): ")

        try:
            # Open the file and read lines into a list
            with open(filename, 'r') as file:
                lines = file.readlines()
                fileFound = True
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied. You might not have the necessary permissions to access this file.")
        except Exception as e:
            print("An error occurred:", str(e))

    num_lines = len(lines)

    while True:
        print("\nNumber of lines in the file:", num_lines)
        line_num = input("Enter a line number (1 to {}), or 0 to quit: ".format(num_lines))
        
        # Check if the input is a valid integer
        if not line_num.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        line_num = int(line_num)

        if line_num == 0:
            print("Exiting program.")
            break
        elif line_num < 1 or line_num > num_lines:
            print("Invalid line number. Please enter a number between 1 and {}.".format(num_lines))
        else:
            print("Line {}:".format(line_num))
            print(lines[line_num - 1].strip())

if __name__ == "__main__":
    main()
