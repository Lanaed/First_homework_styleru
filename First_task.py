import extend_data
import os
print("The budget made", extend_data.make_tmdb_api_request1(method='/movie/215', api_key='14fdc7c908b548547c76e58010815de2')['budget'])
os.system("pause")