#!/usr/bin/python3
"""Module for the first task"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    try:
        sub_info = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)
        if sub_info.status_code == 200:
            return sub_info.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
