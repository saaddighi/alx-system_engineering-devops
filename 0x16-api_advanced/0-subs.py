#!/usr/bin/python3
"requetsts module to make HTTP requests"

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscriber_count = data["data"]["subscribers"]
    else:
        subscriber_count = 0

    return subscriber_count
