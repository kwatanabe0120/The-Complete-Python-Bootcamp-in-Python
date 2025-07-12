import shutil

dir_to_zip = 'extracted_content'
output_filename = 'example'

shutil.make_archive(output_filename, 'zip',dir_to_zip)


shutil.unpack_archive('example.zip','final_unzip','zip')