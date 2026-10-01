# AF Reading and Writing to Files

with open('practice', "r+") as file:
    content = file.read()
    print(content)
    word = content.find("Alex F")
    length = len("Alex F")
    content += " Treyson!"
    file.write(content)

#with open ('practice', "w") as file:
 #   file.write("Hello!!")