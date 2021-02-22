""" Main app/routing file for twitoff """
from flask import Flask, render_template
#FLASK_APP=twitoff flask shell
# create flask application
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        """ at end point '/'"""
        return render_template("base.html", title="Home")
    
    return app

