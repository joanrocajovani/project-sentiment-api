# Project API

## Introduction
In this project, first I downloaded and cleaned a database with the top 1000 movies in IMDB by rating. Then I uploaded it to SQL and created an API so I can request the information. Finally I created a notebook with functions that perform requests.

## Cleaning
The original database had 16 columns and I just kept the following 9:
- Title
- Released Year
- Rating
- Overview
- Director
- Cast (4 columns with 4 actors/actresses)

## Uploading it to SQL
To upload it to SQL, I created a new database called films and a table called movie. Then using the following code in SQL I imported the data.
```SQL
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tablecleanfin.csv'
	INTO TABLE queen
		FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 ROWS;
```

## Establishing Connection
I established connection with the following code:
```
load_dotenv()

dbName = "films"
password=os.getenv("SQL")


connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
```

## Query Endpoints
### 1. Get all the info from the API:
```
http://localhost:9000/sql/
```

### 2. Searching by movie:
**Show all info for selected movie:**
```
http://localhost:9000/sql/title/<name>/
```

**Show selected movie's overview:**
```
http://localhost:9000/sql/title/<name>/overview/
```

**Show selected movie's director:**
```
http://localhost:9000/sql/title/<name>/director/
```

**Show selected movie's cast:**
```
http://localhost:9000/sql/title/<name>/cast/
```

**Show selected movie's rating:**
```
http://localhost:9000/sql/title/<name>/rating/
```

**Show slected movie's released year :**
```
http://localhost:9000/sql/title/<name>/year/
```

**Show sentiment analysis of the selected movie's overview:**
```
http://localhost:9000/sql/title/<name>/sentiment/
```

### 3. Searching by director:
**Show all info for selected director:**
```
http://localhost:9000/sql/director/<name>/
```

**Show selected director's average rating:**
```
http://localhost:9000/sql/director/<name>/avrating/
```

**Show selected director's list of movies:**
```
http://localhost:9000/sql/director/<name>/titles/
```

### 4. Searching by actor/actress:
**Show all info for selected actor/actress:**
```
http://localhost:9000/sql/actor/<name>/
```

**Show selected actor/actress' average rating:**
```
http://localhost:9000/sql/actor/<name>/avrating/
```

**Show selected actor/actress' list of movies:**
```
http://localhost:9000/sql/actor/<name>/titles/
```

## Post Endpoint
### Insert one row to the database:
```
http://localhost:9000/post
```

## Visualization
Finally I created a Jupyther notebook called visualization where there are 3 imported functions to find information searching by movie, director, or actor/actress and also an example of how to post a new row into the database.
