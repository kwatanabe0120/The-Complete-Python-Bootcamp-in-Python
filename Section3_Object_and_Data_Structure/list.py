testlist= [1,2,3,4]
print(testlist)
print(testlist.pop())
print(testlist)


otherlist = ['test', 'really', 'canyou']
newlist = testlist+otherlist
print(newlist)

newlist.append('want to add')
print(newlist)

newlist.pop(0)
print(newlist)

newlist = [1,5,6,45,3,3,454,3,3,2,44,5,65,5,4]
newlist.sort(reverse=True)
print(newlist)
