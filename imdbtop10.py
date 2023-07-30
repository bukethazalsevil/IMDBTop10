import requests
from bs4 import BeautifulSoup
from tkinter import *
import random


target_url = "https://www.imdb.com/list/ls003992425/"

def get_imdb_top_10(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        top_10_movies = []

        for movie in soup.select('.lister-item-header a[href*="title"]'):
            title = movie.text
            top_10_movies.append(title)

        return top_10_movies
    else:
        print("Failed to fetch the data.")
        return []

top_10_movies = get_imdb_top_10(target_url)
for i, movie in enumerate(top_10_movies, 1):
    print(f"{i}. {movie}")


top_10_movies_list = ["The Godfather",
 "The Shawshank Redemption",
 "The Godfather Part II",
 "Inception",
 "Fight Club",
 "The Dark Knight",
 "12 Angry Men",
 "The Lord of the Rings: The Fellowship of the Ring",
 "The Matrix",
 "Se7en"]

def random_choice_movie():
    suggestion = random.choice(top_10_movies)
    showLabel.config(text=suggestion)

window = Tk()
window.title("IMDB TOP 10")
window.config(padx=40,pady=40)

movieLabel = Label(text="Select a movie for me!")
movieLabel.pack()

movieButton = Button(text="Show" , command=random_choice_movie)
movieButton.pack()

showLabel = Label()
showLabel.pack()

window.mainloop()
    
