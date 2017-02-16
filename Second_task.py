import json
import extend_data


api_key = '14fdc7c908b548547c76e58010815de2'
films_file = open("films_details.json", 'w', encoding='utf-8')
films_keywords = open("films_keywords.json", 'w', encoding='utf-8')

amount_of_films, film_number = 0, 0
keywords, films = [], []

while amount_of_films<1000:
    try:
        films.append(extend_data.make_tmdb_api_request(method='/movie/' + str(film_number), api_key=api_key))
        keywords.append(extend_data.make_tmdb_api_request(method='/movie/' + str(film_number)+'/keywords', api_key=api_key))
        amount_of_films += 1
        film_number += 1
    except:
        film_number += 1
json.dump(films, films_file)
json.dump(keywords, films_keywords)