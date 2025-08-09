# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 20:27:29 2025

@author: Pauline Leumani
"""
import praw
import datetime as dt
import pandas as pd

reddit = praw.Reddit(client_id = "",
                     client_secret = "", 
                     user_agent = "", 
                     username = "", 
                     password = "")


kpop_sub_list = ["kpop", "kpopthoughts", "kpop_uncensored", "kpoppers", "unpopularkpopopinions"]
enha_sub_list = ["enhypen", "Enhypenthoughts"]
query = 'enhypen'

# Iterate through kpop subs to get any mentions of Enhypen
enha_reddit_posts = []

for sub in kpop_sub_list:
    subreddit = reddit.subreddit(sub)
    print(f"Fetching from r/{sub}...")
    for post in subreddit.search(query, sort="hot", time_filter="all", limit=None):
        enha_reddit_posts.append([sub, 
                                  post.id,
                                  dt.datetime.fromtimestamp(post.created_utc),
                                  post.title,
                                  post.selftext,
                                  post.score,
                                  post.num_comments
                                  ])
# Get data from Enhypen subs

for en_sub in enha_sub_list:
    en_subreddit = reddit.subreddit(en_sub)
    en = next(en_subreddit.hot(limit=None))
    print(f"Fetching from r/{en_sub}...")
    for en_post in en_subreddit.hot(limit=None):
        enha_reddit_posts.append([en_sub, 
                                 en_post.id,
                                 dt.datetime.fromtimestamp(en_post.created_utc),
                                 en_post.title,
                                 en_post.selftext,
                                 en_post.score,
                                 en_post.num_comments
                                 ])
# Store the data in a csv
df = pd.DataFrame(enha_reddit_posts, columns=["sub", "id", "created_date", "title", "selftext", "score", "num_comments"])
df.to_csv("enha_reddit_posts.csv", index=False)