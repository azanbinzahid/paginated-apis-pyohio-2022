"""
Paginated API: An offset-based strategy
"""

from unittest import result
import requests

results = []
max_results = 500
total = -1  # init

while len(results) != total:
    url = "https://dummyjson.com/products"
    params = {
        'skip': len(results),  # offset value, default to 0
        'limit': 30  # assuming constant limit / number of results
    }

    r = requests.get(url, params=params)

    if r.ok:
        r = r.json()
        total = r['total']  # constant value set
        results.extend(r['products'])
    else:
        print(r.status_code)
        break

    print(F"Status: fetched {len(results)}/{total} results")

# early stop to get only max required results
    if len(results) >= max_results:
        print("Stopping at max pages to fetch")
        break


# verify number of results
assert len(results) == min(total, max_results)
