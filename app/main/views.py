from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_movies, get_movie, search_movie
from ..models import Review
from .forms import ReviewForm
#importing the app instance

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')

    title= 'The days you will never miss, Movies Flow'
    search_movie = request.args.get('movie_query')

    if search_movie:

        return redirect(url_for('.search', movie_name = search_movie))
    else:
        return render_template('index.html', title=title, upcoming= upcoming_movie, popular= popular_movies)

@main.route('/movie/<int:id>')
def movies(id):

    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(id)

    return render_template('movies.html', title=title, movie = movie, reviews = reviews)

    # good stuff.

# search view function
@main.route('/search/<movie_name>')
def search (movie_name):
    """
    view function to display the search results.
    """

    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'

    return render_template('search.html', title = title, movies= searched_movies)

@main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
        form = ReviewForm()
        movie = get_movie(id)

        if form.validate_on_submit():
            title = form.title.data
            review = form.review.data
            new_review = Review(movie.id, title, movie.poster, review)
            new_review.save_review()
            return redirect(url_for('.movies', id = movie.id))
        title = f'{movie.title} review'
        return render_template('new_review.html', title = title, review_form= form, movie = movie)