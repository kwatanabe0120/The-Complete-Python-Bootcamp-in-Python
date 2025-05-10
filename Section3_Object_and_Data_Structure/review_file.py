
with open('review_file.txt', "w") as myfile:
    myfile.write("This is a sample.\nCan you read it?\n")
   
# with open('review_file.txt', "r") as myfile2:   
#     print(myfile2.read())
#     myfile2.seek(0)
#     print(myfile2.readlines())

with open('review_file.txt', 'a') as myfile3:
    myfile3.write("Please add this line")

with open('review_file.txt', 'r') as myfile4:
    # myfile4.seek(0)
    print(myfile4.read())

