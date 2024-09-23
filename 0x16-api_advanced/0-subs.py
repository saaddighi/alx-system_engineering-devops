#!/usr/bin/python3
"requetsts module to make HTTP requests"

import requests
if __name__ == "__main__":
    def number_of_subscribers(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "alx_project"}
        response = requests.get(url, headers, allow_redirects=False)
    
        if response.status_code == 200:
            data = response.json()
            d = data.get("data")
            subscriber_count = d.get("subscribers")
        else:
            subscriber_count = 0      

        return subscriber_count
