from flask import Blueprint, jsonify
from models import User, UserSchema


api = Blueprint('api', __name__)


@api.route("/")
def home():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    user = user_schema.dump(users)
    return jsonify(user)
