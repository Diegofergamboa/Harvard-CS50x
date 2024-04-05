import re

email = input('What is your email? ').strip()

if re.search(r".+@.+\.edu" , email):
    print('valid')
else:
    print('not valid')
