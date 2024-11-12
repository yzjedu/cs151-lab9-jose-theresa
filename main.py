# Programmers:  Jose and Theresa
# Course:  CS151, Dr. Zaleem
# Due Date: 11/13/24
# Lab Assignment: 9
# Problem Statement: Which seat and what table every student sits at
# Data In: Name of file
# Data Out: Name,table number, and seat number
# Credits: In class
# Input Files: vertical list of the names in each Computer Science class

# Purpose: Accept a filename from the user.
# Parameters: None
# Return: Name of the file chosen by the user.
def filename_input():
    filename = input("Please enter the name of the file: ")
    while filename not in ["yalew.txt", "nweke.txt", "isaacman.txt"]:
        print("Invalid file name. Please enter one of the available files.")
        filename = input("Please enter the name of the file ")
    return filename

# Purpose: Read names from the file and return them as a list.
# Parameters: Name of the file to read from.
# Return: List of names read from the file.
def reading_file(filename):
    data = []
    try:
        with open(filename, 'r') as input_file:
            data = [line.strip() for line in input_file.readlines()]
    except FileNotFoundError:
        print("Error reading file. Please make sure the file exists and try again.")
    return data

# Purpose: Assign each name in the list to a specific table and seat.
# Parameters: List of attendee names.
# Return: Displays seating assignments
def assign_seating(names):
    table = 1
    seat = 1
    for name in names:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Table {table}, Seat {seat}, {name}")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~")
        seat += 1
        if seat > 5:
            table += 1
            seat = 1

# Purpose: Main function to run the program, calling the other functions as needed.
# Parameters: None
# Return: None (executes the main flow of the program).
def main():
    print("Hi, how are you? The purpose of this program is to assign your name to a table and seat number.")
    filename = filename_input()  # Accept file name
    names = reading_file(filename)  # Read file contents into a list
    assign_seating(names)  # Assign seating and display
    print("Thank you for using our program, have a nice day!")

# Run the main function
main()


