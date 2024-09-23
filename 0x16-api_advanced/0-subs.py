

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "alx_project"}
    response = requests.get(url, headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscriber_count = data["data"]["subscribers"]
    else:
        subscriber_count = 0
        
    return subscriber_count        
