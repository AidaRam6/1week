from movies import movies

import random

def mov():
    for i in range(len(movies)):
        if movies[i]["imdb"] >= 5.5:
            print(movies[i]["name"])

mov()