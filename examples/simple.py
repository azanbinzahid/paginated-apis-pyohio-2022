"""
Simple non-paginated JSON API
"""

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
print(r.text)
