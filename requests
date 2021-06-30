import requests

url = 'https://www.google.com'

# Get status code
status_code = requests.get(url)

# HTML content
content = requests.get(url).text

# Headers, Data and Post
headers = {"User-Agent": "Python"}
data = {'user': 'admin', 'pass': 'admin'}
post_method = requests.post(url, headers=headers, data=data)
