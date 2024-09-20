#!/usr/bin/python3
"""
Script to interact with the Reddit API using PRAW (Python Reddit API Wrapper).

praw: Python Reddit API Wrapper (PRAW) is a Python package that provides a simple 
interface for accessing Reddit's API.
Usage :
        - This script demonstrates how to:
        - Authenticate with Reddit’s API.
        - Retrieve information about a subreddit.
        - Get the number of subscribers in a specific subreddit.
        - Fetch posts (hot and new) from a given subreddit.
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
