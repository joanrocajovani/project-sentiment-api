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



#INSERTS
def insert_one_row (scene, character_name, dialogue):
    query = f"""INSERT INTO users
     (scene, character_name, dialogue) 
        VALUES ({scene}, '{character_name}', '{dialogue}');
    """
    engine.execute(query)
    return f"Correctly introduced!"