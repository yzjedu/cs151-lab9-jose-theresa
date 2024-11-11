# Algorithm Document
1. 1st task: accepting file name
2. 2nd task: reading name of file into a list
3. 3rd: task: divide list into 5 and assign seating, format and display seats

Output 'Hi how are you? The purpose of this program is to assign your name to a table and seat number'

## Function 1
#### Name: read_file
#### Purpose:accepting the file name 
#### Name: filename_input
#### Parameters: none
#### Return: file
#### Algorithm:
1.  set filename equal to a string input by the user choosing one of the files
2. while filename does not equal a string input:
   3. prompt user to enter one of the three file names 
4. output filename


## Function 2
#### Purpose: making a file into a list  
#### Name: reading_file
#### Parameters: filename_input
#### Return: data
#### Algorithm:
1. define function reading_file :
   2. set data equal to empty list data == []
   3. try:
      4.  set input_file equal to opening the file (open(filename, 'r')) 
         5. set data equal to reading the data in the file by (input_file.readlines)
      6. close file 
      7. return data 
   8. except:
      9. if they close 
      10. output 'Error reading file'
      11. return file 

## Function 3
#### parameter(names in list)
#### name: assign_seating
#### purpose: assign person to specific table and seat
#### return: name with table and seat number
#### Algorithm: 
1. define function assign_person():
2. set variable, table equal to  1
3. set variable, seat equal to 1 
4. for name in names:
   5. output (f'Table'{table}, 'Seat' {seat}, {name})
      6. add 1 to seat variable
      7. if seat equals 5:
         8.  add 1 to table
         9. set seat equal to 1 
         10. return data 


## Function 4
#### Purpose: calling the three functions 
#### Name: Main
#### Parameters: none
#### Return:name at table and seat number
#### Algorithm:
1. define function main():
   2. call filename_input function
   3. call reading_file function
   4. call assign_seating function



### call main function 
### Output 'Thank you for using our program, have a nice day!'
