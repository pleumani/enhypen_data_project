# 🧛 ENHYPEN Data Analysis
Welcome to my project exploring ENHYPEN's album sales, online fan behaviour and Spotify popularity.

[(enha.jpg)](https://github.com/pleumani/enhypen_data_project/blob/main/enha.jpg)

## 🧛‍♀️ About the author
Hi, my name is Pauline Leumani and I have been an ENGENE (ENHYPEN fan) since January 2022. In this project I combined my two passions : **data science** and **ENHYPEN**.

## 🩸 Overview
This project includes : 
- Data collection from Circle Chart, Reddit, Spotify
- Data analysis and visualisations

You will find :
- notebooks : 
  - ENHYPEN Data Project.ipynb : main analysis and visualisations
  - ENHA NLP.ipynb : sentiment analysis (requires Python 3.11; requirements in req_nlp.txt).This notebook contains the sentiment analysis, and generates reddit_posts.csv file with the scores.
- scripts :
  - get_reddit_data.py : collects top Reddit posts across K-pop subreddits
  - get_spotify_data.py : collects track popularity scores
- data :
  - enhypen_album_ranking_byMonth.csv
  - enhypen_album_ranking_byWeek.csv (not used)
  - enhypen_events.csv
  - enha_reddit_posts.csv
  - roberta_results.csv
  - spotify_popularity_scores.csv

Only 2 files are needed (since the data is collected manually) : *enhypen_album_ranking_byMonth.csv* and *enhypen_events.csv*. The rest is collected through Python scripts.

## 🦷 Tools
- Python, Jupyter Notebook
- Pandas, Matplotlib, NLTK, huggingface
- PRAW (Python Reddit API wrapper)
- Spotify API

## How to run
1. Clone the repository.
2. Install requirements
   - For the main notebook :  
   ````
   pip install -r requirements.txt
   ````
   - For the NLP notebook :  
   ````
   pip install -r req_nlp.txt
   ````
## Example output
[(KDE_distribution_per_album.png)](https://github.com/pleumani/enhypen_data_project/blob/main/KDE_distribution_per_album.png)
[(enhypen_albums_boxplot.png)](https://github.com/pleumani/enhypen_data_project/blob/main/enhypen_albums_boxplot.png)
