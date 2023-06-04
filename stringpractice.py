#WRITE THE PROGRAM TO FILL IN A LETTER TEMPLATE.
letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection.
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter your name:\n")
date = input("Enter date:\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)  

#WRITE A PROGRAM TO DETECT DOUBLESPACES IN A STRING.
string = "Program to detect double  spaces."
print(string.find("  "))
print(string.replace("  ", " "))