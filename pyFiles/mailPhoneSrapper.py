#! python3

import re, pyperclip, os

# Create regex for phone numbers

phoneRegex = re.compile(r"""(
           # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext.12345, x12345
           ((\d\d\d)|\(\d\d\d\))?   # Area code (opcional)
           (\s|-)                   # separator (opcional)
           (\d\d\d)                 # first 3 digits
           (-)                        # separator
           (\d\d\d\d)                 # last 4 digits
           (((ext(\.)?\s)|x)        # externsion (opcional)
           (\d{2,5}))?              # extension number (opcional)
           )""", re.VERBOSE)

# Create a regex for mails

mailRegex = re.compile("""
                       # so+_.hing@so+_.hing.com
                       [a-zA-Z0-9_.+]+  # name
                       @                # @
                       [a-zA-Z0-9_.+]+  # domain
                       """, re.VERBOSE)

# Get the text from file (testText.txt)

textsPath = "./pyFiles/txtFiles"
f = open(os.path.join(textsPath, "testText.txt"), "r")
text = f.read()
f.close()

# Extract the mail and phone from the text

moPhone = phoneRegex.findall(text)
moMail = mailRegex.findall(text)

allPhoneNumbers = []
for i in moPhone:
    allPhoneNumbers.append(i[0])
allMails = []
for i in moMail:
    allMails.append(i)
    
phonesText = "\n".join(allPhoneNumbers)
mailsText = "\n".join(allMails)

# Copy the extracted mails and phones to a new file phonesAndMails.txt

result = "Phone numbers:\n{0}\n\nMails:\n{1}".format(phonesText,mailsText)
f = open(os.path.join(textsPath, "testTextFilter.txt"), "wt")
f.write(result)