"""
Ways for handling common HTTP errors
"""

import requests

url = "https://jsonplaceholder.typicode.com/todos/-1"
r = requests.get(url)

# naive
print(r.text)

# basic error handling
if r.ok:
    print(r.text)
else:
    print(r.status_code)

# better try/catch
try:
    if r.ok:
        print(f"Request Successful \n{r.text}")
        # do more stuff as needed
    else:
        r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Request Failed: {err}")
