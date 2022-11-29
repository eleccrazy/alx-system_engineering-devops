#!/usr/bin/python3
"""This python module contains a script that interacts with the Reddit API"""
from requests import get


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Queries the reddit api, parses the title of all hot articles and
    prints a sorted count of a given keywords."""
    header = {"User-Agent": "0x16.api.advanced.project:eleccrazy"}
    params = {"after": after, "count": count, "limit":100}
    res = get("https://www.reddit.com/r/{}/hot/.json".format(subreddit),
              headers=header, allow_redirects=False, params=params)
    if res.status_code == 404:
        print("")
        return
    after = res.json().get("data").get("after")
    count += res.json().get("data").get("dist")
    for r in res.json().get("data").get("children"):
        title = r.get("data").get("title").lower().split()
        for w in word_list:
            if w.lower() in title:
                times = len([t for t in title if t == w.lower()])
                if instances.get(w) is None:
                    instances[w] = times
                else:
                    instances[w] += times
    if after is None:
        if len(instances) == 0:
            print("")
        else:
            s = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            for k, v in instances:
                print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
