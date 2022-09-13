#! python3

message = "Call me at (012) 345-6789 today, or at (098) 765-4321 for my office line."

# Normal solution
def isPhoneNumberSimple(phoneNumber):
    if len(phoneNumber) != 14:
        return False
    if phoneNumber[0] != "(":
        return False
    for i in range(1,4):
        if not phoneNumber[i].isdecimal():
            return False # No area code
    if phoneNumber[4] != ")":
        return False
    if phoneNumber[5] != " ":
        return False
    for i in range(6,9):
        if not phoneNumber[i].isdecimal():
            return False # No area code
    if phoneNumber[9] != "-":
        return False
    for i in range(10,14):
        if not phoneNumber[i].isdecimal():
            return False # No area code
    return True

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+14]
    if isPhoneNumberSimple(chunk):
        print("Phone number found: " + chunk)
        foundNumber = True
if not foundNumber:
    print("Could not find any phone numbers.")
    
# Using regular expressions
import re

phoneNumberRegex = re.compile(r"\((\d\d\d)\) (\d\d\d-\d\d\d\d)") # Always use r"...", () is dividing into groups, \( and \) for serching for parentheses

moPhone = phoneNumberRegex.search(message)

moPhone = phoneNumberRegex.findall(message) # Return a list
for i in moPhone:
    print("Phone number found: ({0}) {1}".format(i[0],i[1]))
    
batRegex = re.compile(r"(Bat)(man|mobile|copter|bat)")
moBat = batRegex.findall("Batman lost his Batmobile so he took his Batcopter and call his friend Batbat")
for i in moBat:
    print("Word found: {0}{1}".format(i[0],i[1]))