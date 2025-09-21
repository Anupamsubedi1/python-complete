#   Introduction to Strings in Python
##   A string is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").
name = "Anupam"

nameshort = name[0:3] 
print(nameshort)
character1 = name[1]
print(character1)

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

#escape sequences
print("Hello \"Anupam\" How are you?") #prints Hello "Anupam" How are you?
print('Hello \'Anupam\' How are you?') #prints Hello 'Anupam' How are you?
print("Hello \\ Anupam How are you?") #prints Hello \ Anupam How are you?
print("Hello \n Anupam How are you?") #prints Hello     Anupam How are you?

#formatted strings
name = input("Enter your name: ")

print(f"Good Afternoon, {name} ") 

print(name.find("  ")) #returns -1 if not found else returns index of first occurence
print(name.replace(" ", "_")) #replaces all spaces with _
print(name.upper()) #converts to uppercase
print(name.lower()) #converts to lowercase  
print(name.capitalize()) #capitalizes first letter of string
print(len(name)) #returns length of string
print(name.endswith("m")) #returns True if string ends with 'm' else False
print(name.startswith("A")) #returns True if string starts with 'A' else False  