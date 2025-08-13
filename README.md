# 🧛 ENHYPEN Data Analysis
Welcome to my project exploring ENHYPEN's album sales, online fan behaviour and Spotify popularity.

## 🩸 Overview
This project contains : 
- Data collection from Circle Chart, Reddit, Spotify
- Data analysis and visualisations

You will find :
- notebooks/ 
  - ENHYPEN Data Project.ipynb : this is the main notebook where you will find analysis and visualisations
  - ENHA NLP.ipynb : this notebook has to be run in a Python 3.11 environment, since the huggingface libraries do not support the latest one yet (you will find all requirements in req_nlp.txt file). This notebook contains the sentiment analysis, and generates reddit_posts.csv file with the scores.
- scripts/
  - get_reddit_data.py : this Python script collects top reddit posts across different kpop subs
  - get_spotify_data.py : this Python script collects popularity scores for every track in albums and EPs
- data/
- images/

## 🧛‍♀️ About the author
Hi, my name is Pauline Leumani and I am an ENGENE since January 2022, which is how ENHYPEN fans are called. In this project I decided to combine my two passions : data science and ENHYPEN.

## 🦷 Tools
Python, Jupyter Notebook, Pandas, Matplotlib, NLTK, huggingface, Python Reddit API wrapper (PRAW), Spotify API
