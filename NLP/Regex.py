import re
text = '''Hi My number is 1234567890 or (123)-456-7890'''
pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, text)
print(matches)