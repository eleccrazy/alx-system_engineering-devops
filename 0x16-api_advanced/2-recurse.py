#!/usr/bin/python3
"""This python module contains a script that interacts with the Reddit API"""
from requests import get


def recurse(subreddit, hot_list=[], after="", count=0):
    """Queries the reddit api and returns a list of containing the titles
    of all hot articles for a given reddit."""
    header = {"User-Agent": "0x16.api.advanced.project:eleccrazy"}
    params = {"after": after, "count": count}
    res = get("https://www.reddit.com/r/{}/hot/.json".format(subreddit),
              headers=header, allow_redirects=False, params=params)
    if res.status_code == 404:
        return None
    after = res.json().get("data").get("after")
    count += res.json().get("data").get("dist")
    for r in res.json().get("data").get("children"):
        hot_list.append(r.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
