"""
Paginated API: A link-based strategy
"""

import requests

results = []
max_results = 500
next = True


while next:
    url = "https://swapi.dev/api/people"
    url = next if len(results) else url # set next url only after first call

    params = {
        # 'limit': 30,  # assuming constant limit / number of results
        # 'next': next,  # it can be a next page id or null / API Specific
    }

    r = requests.get(url, params=params)

    if r.ok:
        r = r.json()
        next = r['next'] if 'next' in r else False  # set next url
        results.extend(r['results'])

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
