"""
Paginated API: An page-based strategy
"""

import requests

results = []
max_pages = 3
page = 0
total = 1  # init

while page < total:
    url = "https://api.instantwebtools.net/v1/passenger"
    params = {
        'page': page,  # offset value, default to 0
        'size': 100  # assuming constant page size
    }

    r = requests.get(url, params=params)

    if r.ok:
        r = r.json()
        total = r['totalPages']  # constant value set
        results.extend(r['data'])

    else:
        print(r.status_code)
        break

    print(F"Status: fetched page {page} of {total} pages")

    # early stop to get only max required results
    if page >= max_pages:
        print("Stopping at max pages to fetch")
        break

    # increment to get next page
    page = page + 1

# verify number of products
assert page == min(total, max_pages)
