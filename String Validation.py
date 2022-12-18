#Ask the user to enter a string
string = input('Please enter a text: ')

#Ask the user to define a key which will be searched inside the string
keyword = input('Please enter one or more characters to be found in the text: ')

#Search the key in the string
if keyword in string:
    
#Return message if key is found 
    print(f'The keyword {keyword} has been found in the text')
    
#Return message if key is NOT found 
else:
    print(f'The keyword {keyword} does not exist in the text')
    
#Handling of the program exit
import sys
exit_program = input('Press any key to exit')
if exit_program:
    sys.exit()
