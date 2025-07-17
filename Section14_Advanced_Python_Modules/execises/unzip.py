import zipfile

f = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
f.extractall()
f.close()