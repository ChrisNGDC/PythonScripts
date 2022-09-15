#! python3

def find(mo, type):
    if mo == []:
        print("Could not find any {0}.".format(type.lower()))
    else:
        for i in mo:
            print("{0} found: {1}".format(type, i[0]))

phoneMessage = "Call me at (+54)(011)22555929 today, or at +5401522555929 for my office line."
mailMessage = "Sen a mail with the information to chrisgabor95@gmail.com or chngdc@frba.edu.ar"

# Using regular expressions
import re

phoneNumberRegex = re.compile(r"(((?:\()?\+[0-9]{2}(?:\))?)((?:\()?[0-9]{3}(?:\))?)([0-9]{8}))") # Always use r"..."
mailRegex = re.compile(r"(((?:[A-Za-z0-9]+[.-_])*[a-zA-Z0-9]+)(@[a-zA-Z]+(?:\.[A-Z|a-z]{2,})+))")

moPhone = phoneNumberRegex.findall(phoneMessage) # Return a list
moMail = mailRegex.findall(mailMessage)

find(moPhone,"Phone Number")
find(moMail,"Mail")

lyrics = "12 drummers drumming, 11 pipers piping, 10 lords leaping , 9 ladies dancing, 8 maids milking, 7 swans swimming, 6 geese laying, 5 golden rings, 4 calling birds, 3 French hens, 2 turtledoves, And 1 partridge in a pear tree"

songRegex = re.compile(r"((\d+)\s(\w+)(\s\w{3,})?)")
moSong = songRegex.findall(lyrics)
print(moSong)
find(moSong, "Words")

vowelRegex = re.compile(r"[aeiouAEIOU]")
consonantRegex = re.compile(r"[^aeiouAEIOU\d\s\W_]")
moVowel = vowelRegex.findall(lyrics)
moConsonant = consonantRegex.findall(lyrics)
print(moVowel)
print(moConsonant)

salute = "Hello, How are you?"
at = "The cat with the hat, sat on the flat mat."
firstLastName = "First Name: Christian Last Name: Gabor"
serve = "<To serve humans> for dinner>"
endsWithWordRegex = re.compile(r"How are you\?$") # Needs to end with
beginsWithHelloRegex = re.compile(r"^Hello") # Needs to start with
saluteRegex = re.compile(r"^Hello, How are you\?$") # Needs to match the entire string
atRegex = re.compile(r".{1,2}at") # . counts anything but a new line
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
nonGreedyServe = re.compile(r"<(.*?)>")
greedyServe = re.compile(r"<(.*)>")
mobeginsWithHello = beginsWithHelloRegex.findall(salute)
moEndsWithWord = endsWithWordRegex.findall(salute)
mosalute = saluteRegex.findall(salute)
moAt = atRegex.findall(at)
moName = nameRegex.findall(firstLastName)
moNonGreedyServe = nonGreedyServe.findall(serve)
moGreedyServe = greedyServe.findall(serve)
print(mobeginsWithHello)
print(moEndsWithWord)
print(mosalute)
print(moAt)
print(moName[0][0],moName[0][1])
print(moNonGreedyServe)
print(moGreedyServe)

normalMessage = "Agent Akali gave the secret documents to Agent Bard"
agentsRegex = re.compile(r"(Agent) (\w)\w*")
moAgentsAll = agentsRegex.findall(normalMessage)
moAgentsRedacted = agentsRegex.sub(r"\1 \2", normalMessage)
print(moAgentsAll)
print(moAgentsRedacted)

# Verbose mode, help it made more readable

re.compile(r"""
           \d\d\d   # Area Code
           -        # First dash
           \d\d\d   # First 3 digits
           -        # Second dash
           \d\d\d\d # Last 4 digits
           """, re.VERBOSE | re.IGNORECASE | re.DOTALL) # Combine various re.