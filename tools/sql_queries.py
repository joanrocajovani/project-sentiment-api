from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM movie;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

#Get info from typed movie
def get_everything_from_movie (name):
    query = f"""SELECT * 
    FROM movie
    WHERE Series_Title = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_description (name):
    query = f"""SELECT Overview 
    FROM movie
    WHERE Series_Title = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_director (name):
    query = f"""SELECT Director 
    FROM movie
    WHERE Series_Title = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_cast (name):
    query = f"""SELECT Star1, Star2, Star3, Star4 
    FROM movie
    WHERE Series_Title = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_rating (name):
    query = f"""SELECT IMDB_Rating 
    FROM movie
    WHERE Series_Title = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_year (name):
    query = f"""SELECT Released_Year 
    FROM movie
    WHERE Series_Title = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# SQL get movies from selected director
def get_director_everything (name):
    query = f"""SELECT * 
    FROM movie
    WHERE Director = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records") 

def get_director_titles (name):
    query = f"""SELECT Series_Title 
    FROM movie
    WHERE Director = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_director_avgrating (name):
    query = f"""SELECT AVG(IMDB_Rating) 
    FROM movie
    WHERE Director = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

#Get movies from selected actor
def get_actor_everything (name):
    query = f"""SELECT *
    FROM movie
    WHERE Star1 = '{name}' OR Star2 = '{name}' OR Star3 = '{name}' OR Star4 = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_actor_titles (name):
    query = f"""SELECT Series_Title
    FROM movie
    WHERE Star1 = '{name}' OR Star2 = '{name}' OR Star3 = '{name}' OR Star4 = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_actor_avgrating (name):
    query = f"""SELECT AVG(IMDB_Rating)
    FROM movie
    WHERE Star1 = '{name}' OR Star2 = '{name}' OR Star3 = '{name}' OR Star4 = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")    
 
#INSERTS
def insert_one_row (Series_Title, Released_Year, IMDB_Rating, Overview, Director, Star1, Star2, Star3, Star4):
    query = f"""INSERT INTO movie
     (Series_Title, Released_Year, IMDB_Rating, Overview, Director, Star1, Star2, Star3, Star4) 
        VALUES ('{Series_Title}', '{Released_Year}', '{IMDB_Rating}', '{Overview}', '{Director}', '{Star1}', '{Star2}', '{Star3}', '{Star4}');
    """
    engine.execute(query)
    return f"Correctly introduced!"