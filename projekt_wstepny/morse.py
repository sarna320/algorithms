import sys
import morse_dict as md

with open(sys.argv[1], "r") as file:  # opening file from your working folder
    data = file.read()
encrypted = ""  # intialization of encrypted value in morse code
data = data.upper()  # all leters to upper
data = data.strip(" ")  # this solves spaces in first line at start, if there would be
for i in range(0, len(data)):
    if ord(data[i]) >= 65 and ord(data[i]) <= 90:  # check if char is letter
        encrypted += f"{md.MORSE_CODE_DICT[data[i]]}"  # if yes we add encrypted value from dictionary
        if (i<len(data)-1): #this is necessary to do it this way to exactly match example output
            if(data[i+1]!=" "and data[i+1]!="\n"):
                encrypted+=" "
    elif (data[i] == " "and (ord(data[i + 1]) >= 65 and ord(data[i + 1]) <= 90)):  # check if current char is space and next is a letter
        if (encrypted[-1] == "\n"):  # checking situation "  a kot ma Ale", double space at new line is the problem
            pass
        else:
            encrypted += " / "  # after checking all problem we add "/ "
    elif data[i] == "\n":  # for new line add new line
        encrypted += "\n"

print(encrypted)