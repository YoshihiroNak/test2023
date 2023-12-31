from flask import abort
from flask_jwt_extended import  get_jwt_identity
from models.user import User
from setup import db

def authorize(user_id=None):
    jwt_user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=jwt_user_id)
    user = db.session.scalar(stmt)
    # If it's not the case that the user is an admin ot user_id truthy and matches the token
    # i.e. if user_id isn't passed in, they must be admin
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        abort(401)
    