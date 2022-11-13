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

#SQL get from selected movie
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


# SQL get movies from selected director
@app.route("/sql/director/<name>/", )
def director_everything (name):
    return jsonify(esecuele.get_director_everything(name))

@app.route("/sql/director/<name>/titles/", )
def director_titles (name):
    return jsonify(esecuele.get_director_titles(name))

@app.route("/sql/director/<name>/avgrating/", )
def director_avgrating (name):
    return jsonify(esecuele.get_director_avgrating(name))

#Get movies from selected actor
@app.route("/sql/actor/<name>/", )
def actor_everything (name):
    return jsonify(esecuele.get_actor_everything(name))

@app.route("/sql/actor/<name>/titles/", )
def actor_titles (name):
    return jsonify(esecuele.get_actor_titles(name))

@app.route("/sql/actor/<name>/avgrating/", )
def actor_avgrating (name):
    return jsonify(esecuele.get_actor_avgrating(name))

# POST
@app.route("/post", methods=['POST'])
def insert_row():
    my_params = request.args
    print(my_params)
    Series_Title = my_params["Series_Title"]
    Released_Year = my_params["Released_Year"]
    IMDB_Rating = my_params["IMDB_Rating"]
    Overview = my_params["Overview"]
    Director = my_params["Director"]
    Star1 = my_params["Star1"]
    Star2 = my_params["Star2"]
    Star3 = my_params["Star3"]
    Star4 = my_params["Star4"]

    esecuele.insert_one_row(Series_Title, Released_Year, IMDB_Rating, Overview, Director, Star1, Star2, Star3, Star4)
    return f"Query succesfully inserted"



if __name__ == "__main__":
    app.run(port=9000, debug=True)