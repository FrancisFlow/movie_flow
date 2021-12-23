from flask import render_template
from app import app
#importing the app instance

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/movies/<movie_id>')
def movies(movie_id):

    return render_template('movies.html', id=movie_id)