#!/usr/bin/python3

"""
Script to get the number of subscribers for a specific subreddit using PRAW (Python Reddit API Wrapper).

Modules:
    - praw: Python Reddit API Wrapper (PRAW) is a Python package that provides a simple interface to interact with Reddit's API.

Setup:
    - Install PRAW using: `pip install praw`
    - You must have a Reddit account and create an app to get the necessary credentials: client_id, client_secret, and user_agent.

Functionality:
    - The script defines a function `number_of_subscribers` that:
        - Takes a subreddit name as input.
        - Authenticates with Reddit's API using PRAW.
        - Retrieves the number of subscribers for the given subreddit.
        - Returns the number of subscribers, or 0 if the subreddit is not found or an error occurs.

Authentication:
    - client_id: Your Reddit app’s client ID.
    - client_secret: Your Reddit app’s client secret.
    - user_agent: A string identifying the app/script (e.g., "alx_project").

How to Use:
    1. Call the `number_of_subscribers(subreddit)` function with the subreddit name as an argument.
    2. The function will return the number of subscribers for the specified subreddit.
    3. Example:
        subscriber_count = number_of_subscribers("learnpython")
        print(f"Number of subscribers: {subscriber_count}")
"""

import praw

if __name__ == "__main__":
    def number_of_subscribers(subreddit):
        reddit = praw.Reddit(
            client_id = "eBcNZzIKJzH23dGoHND91w",
            client_secret = "Ui3vaGH19po-U178PYWUROGrTJhGZw",
            user_agent = "alx_project"
        )
        subreddit = reddit.subreddit(subreddit)
        try:
            subscriber_count = subreddit.subscribers
        except:
            subscriber_count = 0

        return subscriber_count
