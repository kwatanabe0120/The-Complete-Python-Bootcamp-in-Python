import shutil
import re
import os

# unzip the instrction file
# shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

# Show the instruction file in console
# with open('extracted_content/Instructions.txt') as f:
# 	content = f.read()
# 	print(content)

# make regular expression
pattern = r'\d{3}-\d{3}-\d{4}'

# check if the regular expressin works
# test = '123-123-1234'
# print(re.findall(pattern, test))

# func for search patter in a file
def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
	f = open(file,'r')
	text = f.read()
	
	if re.search(pattern, text):
		return re.search(pattern, text)
	else:
		return ''


result = []
for folder, sub_folders, files in os.walk(os.getcwd()+'/extracted_content'):
	for f in files:
		full_path = folder+'/'+f
		result.append(search(full_path))

for r in result:
	if r != '':
		print(r.group())