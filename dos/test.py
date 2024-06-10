# import requests
#
# # Create a session
# with requests.Session() as session:
#     # GET request to retrieve information from the website
#     response = session.get('https://youtube.com')
#
#     # Print the response text
#     print(response.text)
#
#     # POST request with data, for example, to log in to a website
#     login_data = {'username': 'ickey', 'password': 'ouse'}
#     response = session.post('https://example.com/login', data=login_data)
#
#     # Another GET request, this time with the login session
#     response = session.get('https://example.com/dashboard')
#
#     # Print the response text after logging in
#     print(response.text)

import pycurl
from io import BytesIO

while True:
    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "https://www.youtube.com")
    c.setopt(pycurl.WRITEDATA, b)
    c.perform()
    c.close()
