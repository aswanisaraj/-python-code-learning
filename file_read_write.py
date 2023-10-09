'''Make a txt file add the file name in these blanks. You will be able to read and write in the txt file.'''

f = open("_____", "a")
a =f.write("Saraj bhai boht achhy hen\n")
print(a)
f.close()

f = open("______", "r+")
print(f.read())
f.write("Thank you\n")
