file = open("C:/Users/sunde/OneDrive/Desktop/pythonprograms/FileHandling/geeks.txt", 'r')
content = file.read()
print(content)
file.close()

# with open("geeks.txt","a") as file:
#     file.write("THi will add this line")
#     content = file.read()
#     print(content)