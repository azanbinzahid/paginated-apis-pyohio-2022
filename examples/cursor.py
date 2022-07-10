"""
Paginated API: An cursor-based strategy
"""

import requests

results = []
max_results = 500
next = True

while next:
    url = "https://cursor-based-api/example"  # not a real endpoint
    params = {
        'limit': 30,  # assuming constant limit / number of results
        'next': next  # it can be a url, an id or a cursor
    }

    r = requests.get(url, params=params)

    if r.ok:
        r = r.json()
        next = r['next'] if 'next' in r else False
        results.extend(r['products'])
    else:
        print(r.status_code)
        break

    print(F"Status: fetched {len(results)} results so far")

    # early stop to get only max required results
    if len(results) >= max_results:
        print("Stopping at max pages to fetch")
        break


# verify number of results
assert len(results) == min(len(results), max_results)
