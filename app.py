from flask import Flask ,render_template
from flask_bootstrap import Bootstrap



# def create_app():
#     app=Flask(__name__)
# 	Bootstrap(app)
# 	return app

app=Flask(__name__)
bootstrap=Bootstrap(app)
@app.route("/")
def home():

	movie_names = ['Avatar', 
		           'Pirates of the Caribbean',
		           'Spectre',
		           'The Dark Knight Rises',
		           'John Carter',
		           'Spider-Man 3',
		           'Tangled' ]

	# Movie Titles with Attributes - Stored in a Dictionary
	movies = {
		'Avatar': { 'critical_reviews': 723, 'duration': 178, 'imdb_score': 7.9 },
		'Pirates of the Caribbean': { 'critical_reviews': 302, 'duration': 169, 'imdb_score': 7.1 },
		'Spectre': { 'critical_reviews': 602, 'duration': 148, 'imdb_score': 6.8 },
		'The Dark Knight Rises': { 'critical_reviews': 813, 'duration': 164, 'imdb_score': 8.5 },
		'John Carter': { 'critical_reviews': 462, 'duration': 132, 'imdb_score': 6.6 },
		'Spider-Man 3': { 'critical_reviews': 392, 'duration': 156, 'imdb_score': 6.2 },
		'Tangled': { 'critical_reviews': 324, 'duration': 100, 'imdb_score': 7.8 },
		}
    
	return render_template('index.html',movie_names=movie_names,movies=movies)


@app.route("/<channel>/<username>/")
def channel(username):
    return render_template("username.html",username=username)

@app.errorhandler(404)
def page_not_handler():
	return render_template("404.html"),404



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)