from datetime import datetime
from config import db, login_manager
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

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


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.Text, nullable=True)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Service('{self.title}', '{self.description}', '{self.icon}',)"


class ServiceSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Services
        session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    icon = fields.String(required=True)
    date_created = fields.String(required=True)


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

    def __repr__(self):
        return f"Project('{self.name}', '{self.description}', '{self.image_link}', '{self.view_link}', '{self.frontend}', '{self.backend}', '{self.source_code}',)"

class ProjectSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Project
        session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    image_link = fields.String(required=True)
    view_link = fields.String(required=True)
    frontend = fields.String(required=True)
    source_code = fields.String(required=True)
    date_created = fields.String(required=True)

class About(db.Model):
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
        return f"Bio('{self.name}',  '{self.description}', '{self.birth}', '{self.address}', '{self.image_link}',, '{self.email}', '{self.phone}')"


class AboutSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = About
        session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    birth = fields.String(required=True)
    address = fields.String(required=True)
    email = fields.String(required=True)
    image_link = fields.String(required=True)
    phone = fields.String(required=True)
    date_created = fields.String(required=True)


class Education (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), primary_key=True)
    date_start = db.Column(db.Text, nullable=False)
    date_end = db.Column(db.Text, nullable=False)
    programs = db.Column(db.Text, nullable=True)
    major = db.Column(db.Text, nullable=True)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Education('{self.title}', '{self.date_start}', '{self.date_end}', '{self.programs}', '{self.major}')"

class EducationSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Education
        session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    date_start = fields.String(required=True)
    date_end = fields.String(required=True)
    programs = fields.String(required=True)
    major = fields.String(required=True)
    date_created = fields.String(required=True)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), primary_key=True)
    date_start = db.Column(db.Text, nullable=False)
    date_end = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Experience('{self.title}', '{self.date_start}', '{self.date_end}', '{self.position}', '{self.description}')"

class ExperienceSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Experience
        session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    date_start = fields.String(required=True)
    date_end = fields.String(required=True)
    position = fields.String(required=True)
    description = fields.String(required=True)
    date_created = fields.String(required=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    message = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"('{self.name}', '{self.message}', '{self.email}')"


