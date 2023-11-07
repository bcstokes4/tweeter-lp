# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from .forms.form import Tweet
import random
from random import randint
from datetime import date


app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    """ renders home page, 
        randomly picks tweet dictionary from tweets list
        and renders on page
    """
    tweet = random.choice(tweets)
    return render_template("index.html", tweet=tweet)

@app.route('/feed')
def feed():
    return render_template("feed.html", tweets=tweets)


@app.route("/new", methods=["GET", "POST"])
def create_tweet():
    form = Tweet()

    if form.validate_on_submit():
        new_tweet = {
            'id': len(tweets) + 1,
            "author": form.data["author"],
            "date": date.today(),
            "tweet": form.data["tweet"],
            "likes": randint(10000, 999_999),
        }
        tweets.append(new_tweet)
        return redirect('/feed')  

    if form.errors:
        print(form.errors)
        return render_template("new_tweet.html", form=form, errors=form.errors)

    return render_template("new_tweet.html", form=form, errors=None)

    




