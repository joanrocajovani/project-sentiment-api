from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as esecuele
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

@app.route("/sql/<name>", )
def movie_all (name):
    return jsonify(esecuele.get_everything_from_movie(name))

@app.route("/sql/<name>/overview/", )
def movie_overview (name):
    return jsonify(esecuele.get_just_description(name))

@app.route("/sql/<name>/director/", )
def movie_director (name):
    return jsonify(esecuele.get_just_director(name))

@app.route("/sql/<name>/cast/", )
def movie_cast (name):
    return jsonify(esecuele.get_just_cast(name))

@app.route("/sql/<name>/rating/", )
def movie_rating (name):
    return jsonify(esecuele.get_just_rating(name))

@app.route("/sql/<name>/year/", )
def movie_year (name):
    return jsonify(esecuele.get_just_year(name))  

@app.route("/sql/<name>/sentiment/", )
def get_sentiment_overview (name):
    df = esecuele.get_just_description(name)
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()

    def sa(x):
        try:
            return sia.polarity_scores(x)
        except:
            return x
    print(df)
    #df["polarity_score"] = df["Overview"].apply(sa)
    var = sia.polarity_scores(df[0]["Overview"])
    print(df)
    #return jsonify(df.to_dict(orient='records'))
    return str(var)
    

if __name__ == "__main__":
    app.run(port=9000, debug=True)