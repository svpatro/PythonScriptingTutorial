# Goal: Fill in the blanks using the provided resources in Directions.pdf

import re
pattern = '' # Fill in this using the regular exression guidebook

f = open('', 'r') # Insert the file you are reading from.
string = f.read()
found = re.search(pattern, string)

if (found):
    
    print("expression found!")

    # if the statement is found, write to new file.

else:
    print("nothing found")
