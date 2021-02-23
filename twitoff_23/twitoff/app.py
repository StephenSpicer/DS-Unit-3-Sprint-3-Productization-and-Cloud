""" Main app/routing file for twitoff """
from flask import Flask, render_template
from .models import DB, User, Tweet, insert_example_users

#FLASK_APP=twitoff flask shell

# create flask application
def create_app():
    """ Flask application """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATASASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app()



    @app.route("/")
    def root():
        """ at end point '/'"""
        users = User.query.all()
               
        return render_template("base.html", title="Home", user=users)
    
    @app.route("/reset")
    def reset():
        """reset DB using drop_all()"""
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        return render_template("base.html", title="RESET", user=User.query.all())

    return app

