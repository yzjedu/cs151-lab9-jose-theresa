# Algorithm Document
1st task: accepting file name
2nd task: reading name of file into a list
3rd: task: divide list into 5 and assign seating, format and display seats

Print('Hi how are you? The purpose of this program is to assign your name to a table and seat number')

Function 1
Name: read_file
# Purpose:accepting the file name 
# Name: reading_file
# Parameters: none
# Return: file
# Algorithm:
1. filename= str(input('Please enter one of the three file names'))
2. while filename != str:
   3. filename = str(input('Please enter one of the three file names'))
4. output filename


Function 2
# Purpose:reading  
# Name: reading_file
# Parameters: filename_input
# Return: data
# Algorithm:
1. def read_file_to_list(filename):
   2. data == []
   3. try:
      4. input_file = open(filename, 'r')
         5. data = input_file.readlines
      6. input_file.close()
      7. return data 
      8. except:
         9. input_file.close)
         10. print('Error reading file')
         11. return file 

Function 3
# parameter(names in list)
# name: assign_seating
# purpose: assign person to specific table and seat
# return: name with table and seat number
# Algorithm: 
1. def assign_person():
2. table = 1
3. seat = 1 
4. for name in names:
   5. print(f'Table'{table}, 'Seat' {seat}, {name})
      5. something
      6. seat += 1
      7. if seat == 5:
         8. table += 1
         9. seat = 1
         10. return data 



# Purpose: calling the three functions 
# Name: Main
# Parameters: none
# Return:name at table and seat number
# Algorithm:
- Def Main():
reading_file()
function3()