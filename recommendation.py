import json

def find_user_title_in_base(films, user_title):
    film_number = 0
    for film in films:
        if film['title'].lower().find(user_title.lower()) != -1 or film['original_title'].lower().find(user_title.lower()) != -1:
            print(film['title'])
            film_number += 1
    if film_number == 0:
        print('I can\'t do it')

def search_of_recommendations (your_genres, your_keywords, films, keywords):
    find_genres = set(i['name'] for i in your_genres)
    find_keywords = set(i['name'] for i in your_keywords)
    for i, j in zip(films, keywords):
        set_of_genres = set(g['name'] for g in i['genres'])
        set_of_keywords = set(k['name'] for k in j['keywords'])
        if (len(set_of_genres & find_genres) >= 1) and (len(set_of_keywords & find_keywords) >= 2):
            print(i['title'])

def analyze_result(success_of_search):
    if success_of_search:
        print('Have a nice watching:)')
    else:
        print('Sorry, but we can\'t find your film. Please, try again title.')
