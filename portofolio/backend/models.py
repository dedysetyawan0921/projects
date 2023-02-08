from datetime import datetime
from flask import current_app
from config import db, login_manager
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class UserSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = User
        session = db.session
    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    date_created = fields.String(required=True)

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.Text, nullable=True)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text, nullable=False)
    view_link = db.Column(db.Text, nullable=False)
    frontend = db.Column(db.Text, nullable=True)
    backend = db.Column(db.Text, nullable=True)
    source_code = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)


class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    birth = db.Column(db.String(121), nullable=False)
    address = db.Column(db.String(121), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_link = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text,  nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Bio('{self.name}')"

    


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    message = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
