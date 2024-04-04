import re

email = input('What is your email? ').strip()

if re.search(".+@.+", email):
    print('valid')
else:
    print('not valid')
