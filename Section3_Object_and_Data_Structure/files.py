# Creating a sample text file
sample_text = """This is a sample text file.
It contains multiple lines of text.
You can use it for testing purposes."""

# Writing the sample text to a file
with open("sample.txt", "w") as file:
    file.write(sample_text)

print("Sample text file 'sample.txt' created successfully.")

myfile = open('sample.txt')

print(myfile.read())
#nothing happened because cursor is end of file 
print(myfile.read())

myfile.seek(0)
print(myfile.read())
myfile.seek(0)

# make one line for one contents in list
content = myfile.readlines()
print(content)

myfile.close()