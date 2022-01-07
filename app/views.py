from flask import render_template, request, redirect, url_for
from app import app
from .request import get_movies, get_movie, search_movie

#importing the app instance

@app.route('/')
def index():

    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')

    title= 'The days you will never miss, Movies Flow'
    search_movie = request.args.get('movie_query')

    if search_movie:

        return redirect(url_for('search', movie_name = search_movie))
    else:
        return render_template('index.html', title=title, upcoming= upcoming_movie, popular= popular_movies)

@app.route('/movie/<int:id>')
def movies(id):

    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movies.html', title=title, movie = movie)

    # good stuff.

# search view function
@app.route('/search/<movie_name>')
def search (movie_name):
    """
    view function to display the search results.
    """

    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'

    return render_template('search.html', movies= searched_movies)