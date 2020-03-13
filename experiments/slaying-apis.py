#https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

import requests
import sys

user_url = input('Please enter a URL to check status: (e.g. http://api.open-notify.org/): ')
request = requests.get(user_url)
status_code = request.status_code
if status_code is not 200:
    print('I\'m sorry - it appears I cannot connect to ') + request + (' - the status code is: ') + str(status_code)
    sys.exit(1)
else:
    if status_code is 200:
        scrape_page = input('Great! Status code is ' + str(status_code) + ' would you like me to scrape the webpage? y/n: ')
        if scrape_page is 'y':
            print(request.text)
            sys.exit(0)
        elif scrape_page is 'n':
            print('No problem. Thanks for your time')
            sys.exit(0)
        else:
            print('Unrecognised input. Exiting')
            sys.exit(1)
