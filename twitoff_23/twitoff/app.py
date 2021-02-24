"""Main app/routing file for Twitoff"""

from os import getenv
from flask import Flask, render_template
from .models import DB, User
from .twitter import update_all_users, add_or_update_user


def create_app():
    """Create Flask Application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route("/")
    def root():
        """At end point '/'"""
        return render_template("base.html", title="Home", users=User.query.all())

    @app.route('/update')
    def update():
        """Updates each user"""
        update_all_users()
        return render_template("base.html", title="Users Updated!", users=User.query.all())

    @app.route("/reset")
    def reset():
        """reset DB using drop_all()"""
        DB.drop_all()
        DB.create_all()
        add_or_update_user("elonmusk")
        add_or_update_user("AOC")
        return render_template("base.html", title="RESET", users=User.query.all())

    return app