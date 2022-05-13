from app import app
from flask import render_template, url_for



@app.route('/')
@app.route('/index') 
@app.route('/test')

def index():
    user = {
        'username': "Melvin"
    }
    quotes_i_like = [
        {
            'author': {'username': "mum"}, 'text' : "he means well"
        },
        {
            'author': {'username': "me"}, 'text' : "mathamagiciaon"
        },
        {
            'author': {'username': "dad"}, 'text' : "maths is fun"
        }

    ]
    return render_template("index.html", title="melvins page", user=user, quotes=quotes_i_like)




