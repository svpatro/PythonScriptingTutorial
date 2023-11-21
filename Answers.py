# Goal: Fill in the blanks using the provided resources.

import re
pattern = '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}' # Fill in this using the regular exression guidebook

f = open('./TextFiles/numbers.txt', 'r')  # Insert the file you are reading from
string = f.read()
found = re.search(pattern, string)

if (found):

    print("expression found!")

    # if the statement is found, write it to a new file

    with open('./TextFiles/found.txt', 'w') as h:
        h.write(string)

else:
    print("nothing found")
