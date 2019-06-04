from flask import render_template
from app import app

# Views
# Home route
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Welcome to flask app'
    title = 'Flask App'
    '''
        first message represent the variable in the template and the second represent the variable in the function
    '''

    return render_template('index.html', message=message, title=title)


# Movie route
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    title = 'Movie'
    return render_template('movie.html',id = movie_id, title=title)
