import re

text = 'my phone number is 408-555-7777'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d', text)
print(phone)
print(phone.group())


text = 'my phone number is 408-555-7777'
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())


phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))