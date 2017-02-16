import json
import recommendation
import os

print("Input the name of film")
entered_film, success_of_search = input(), False
films = json.load(open("films_details.json", "r"))
keywords = json.load(open("films_keywords.json", "r"))
for i, j in zip(films, keywords):
    if i['title'].lower() == entered_film.lower() or i['original_title'].lower() == entered_film.lower():
        entered_genres = i['genres']
        entered_keywords = j['keywords']
        success_of_search = True
        if not entered_genres and not entered_keywords:
            print ('We look for on occurrence of a subline')
            recommendation.find_user_title_in_base(films, entered_film)
        else:
            recommendation.search_of_recommendations(entered_genres, entered_keywords, films, keywords)
        break
recommendation.analyze_result(success_of_search)
os.system("pause")
