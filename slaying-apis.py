#https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

import requests
import sys

request = requests.get('http://api.open-notify.org/')
status_code = request.status_code
if status_code is 200:
    print(' Status code is: ' + str(status_code))
    user_answer = input('Would you like to scrape page? y/n: ')
    if user_answer is 'y':
        print(request.text)
    else:
        sys.exit(0)
else:
    print('Error: status code is  ' + str(status_code))
    sys.exit(1)
