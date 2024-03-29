"""
Paginated API: A cursor-based strategy
"""

import requests

results = []
max_results = 500
next = True
start = 0

while next:
    url = "https://cursor-based-api/example"  # not a real endpoint
    params = {
        'limit': 30,  # assuming constant limit / number of results
        'after': start,  # request id after start value
        # 'before': before,  # same as above
    }

    r = requests.get(url, params=params)

    if r.ok:
        r = r.json()
        # could be has_more attrib / API specific
        next = r['next'] if 'next' in r else False
        start = r['before']  # after value for next call / API specific
        results.extend(r['products'])
    else:
        print(r.status_code)
        break

    print(F"Status: fetched {len(results)} results so far")

    # early stop to get only max required results
    if len(results) >= max_results:
        print("Stopping at max results to fetch")
        break


# verify number of results
assert len(results) == min(len(results), max_results)
