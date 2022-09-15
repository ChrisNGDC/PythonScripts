#! python3

import re, pyperclip

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

# Get the text from clipboard

text = pyperclip.paste()

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

# Copy the extracted mails and phones to the clipboard

result = "Phone numbers:\n{0}\n\nMails:\n{1}".format(phonesText,mailsText)

pyperclip.copy(result)