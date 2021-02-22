""" SQLAlchemy Database """
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

#User Table using SQLAlchemy syntax

class User(DB.Model):
    """ Twitter Users that correspond to tweets """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)
