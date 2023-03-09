#!/usr/bin/python3
"""
 Reddit API and prints the titles
"""

import json
import requests
import sys


def top_ten(subreddit):
    """
    returning the hot post
    """
    if len(sys.argv) < 2:
        return print(None)
    else:
        url_link = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url_link, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return print(None)
        body = json.loads(res.text)
        for i in body["data"]["Employees"]:
            print(i["data"]["title"])
