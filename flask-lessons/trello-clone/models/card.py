from setup import db, ma
from datetime import datetime
from marshmallow import fields
from marshmallow.validate import OneOf, Regexp, Length, And

VALID_STATUSES = ('To Do', 'Done', 'Progress', 'Testing', 'Deployed', 'Cancelled')

class Card(db.Model):
    __tablename__ = 'cards'

    id =db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(30), default='To Do')
    data_created = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))
    # users is table name
    # Foreign Key - establishes a relationship at the database level
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # SQLAlchemy relationship - nest an instance of a User model tn this one
    user = db.relationship('User', back_populates='cards')
    comments = db.relationship('Comment', back_populates='card')

class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])
    comments = fields.Nested('CommentSchema', many=True, exclude=['card'])
    status = fields.String(validate=OneOf(VALID_STATUSES))
    # Title must contain only letters, numbers and spaces
    title = fields.String(required=True, validate=And(
        Regexp('^[0-9a-zA-Z ]+$', error='Title must contain only letters, numbers and spances'),
        Length(min=3, error='Title must be at least 3 characters long')
    ))

    class Meta:
        fields = ('id', 'title', 'description', 'status', 'data_created', 'user', 'comments')
        