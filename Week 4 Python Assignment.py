# File Read & Write Challenge:Create a program that reads a file and writes a modified version to a new file.

with open("newFile.txt", "w") as file:
  content = file.write("I love coding!\n")
  
  
file = open("newFile.txt", "r")
content = file.read()
print(content)
modified_content = content.upper()


with open("finalFile.txt", "w") as file:
 data = file.write(modified_content)

file = open("finalFile.txt", "r")
data = file.read()
print(data)



#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    file = open("input.pdf" "r")
    details = file.read()
    print(details)
except FileNotFoundError:
    print("File not found. please a valid file name")



