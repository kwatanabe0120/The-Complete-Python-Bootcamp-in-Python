import zipfile

f = open('file_one.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('file_two.txt', 'w+')
f.write('TWO FILE')
f.close()

# make empty zip file
comp_file = zipfile.ZipFile('comp_file.zip','w')

# add file to empty zip file
comp_file.write('file_one.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file_two.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
