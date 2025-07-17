import re
import os

phone_num = []
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# Define the base path to extracted content
base_path = 'extracted_content'

# Define folder names to iterate through
folders = ['One', 'Two', 'Three', 'Four', 'Five']

# Iterate through each folder
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    
    if os.path.exists(folder_path):
        print(f"Searching in folder: {folder}")
        
        # Get all .txt files in the current folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                
                try:
                    # Read the file content
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        
                        # Find all phone numbers in the content
                        matches = pattern.findall(content)
                        
                        # Add found phone numbers to the list
                        for match in matches:
                            phone_num.append(match)
                            print(f"Found phone number: {match} in {filename}")
                            
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    else:
        print(f"Folder {folder} not found in {base_path}")

# Print summary
print(f"\nTotal phone numbers found: {len(phone_num)}")
print("All phone numbers:")
for phone in phone_num:
    print(phone)
