import json
import recommendation
import os

films = json.load(open('films_details.json'))
print('Enter title of film : ')
entered_title = input()
print('Results :')
recommendation.find_user_title_in_base(films, entered_title)
os.system("pause")