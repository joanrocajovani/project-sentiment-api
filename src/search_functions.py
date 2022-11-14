import requests
import pandas as pd
import numpy as np

#Function to get info from selected movie
def find_info_movie():
    movie = input("Please enter a movie: ")
    options = ['everything', 'director', 'rating', 'year', 'overview', 'cast', 'sentiment']

    user_input = ''

    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input.lower() not in options:
        user_input = input(input_message)
    
    if user_input == 'everything':
        url = f'http://localhost:9000/sql/title/{movie}/'
        res = requests.get(url)
        info = res.json()
        return info[0]
        
    elif user_input == 'sentiment':
        url = f'http://localhost:9000/sql/title/{movie}/{user_input}/'
        res = requests.get(url)
        info = res.content
        return info
    
    else:
        url = f'http://localhost:9000/sql/title/{movie}/{user_input}/'
        all_info_movie = requests.get(url)
        info = all_info_movie.json()
        return info[0]

#Function to get info from selected director
def find_info_director():
    director = input("Please enter a director: ")
    options = ['everything', 'avgrating', 'titles']

    user_input = ''

    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input.lower() not in options:
        user_input = input(input_message)
    
    if user_input == 'everything':
        url = f'http://localhost:9000/sql/director/{director}/'
        res = requests.get(url)
        df = pd.DataFrame.from_dict(res.json())
        return df
    
    else:
        url = f'http://localhost:9000/sql/director/{director}/{user_input}/'
        all_info_movie = requests.get(url)
        info = all_info_movie.json()
        return info

#Function to find info from selected actor/actress
def find_info_actor():
    actor = input("Please enter an actor or actress: ")
    options = ['everything', 'avgrating', 'titles']

    user_input = ''

    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input.lower() not in options:
        user_input = input(input_message)
    
    if user_input == 'everything':
        url = f'http://localhost:9000/sql/actor/{actor}/'
        res = requests.get(url)
        df = pd.DataFrame.from_dict(res.json())
        return df
    
    else:
        url = f'http://localhost:9000/sql/actor/{actor}/{user_input}/'
        all_info_movie = requests.get(url)
        info = all_info_movie.json()
        return info
