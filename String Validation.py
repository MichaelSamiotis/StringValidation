#Ask the user to enter a string
string = input("Please enter a text: ")

#Ask the user to define a key which will be searched in the string
keyinstring = input("Please enter one or more characters to be found in the text: ")

#Search the key in the string
if keyinstring in string:
#Return message if key is found 
    print("The \'{:s}\' has been found in the \'{:s}\' text".format(keyinstring,string))
#Return message if key is NOT found 
else:
    print("The \'{:s}\' does not exist in the \'{:s}\' text".format(keyinstring,string))
    
input("Please press Enter")
