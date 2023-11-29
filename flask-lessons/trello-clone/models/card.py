from setup import db, ma
from datetime import datetime
from marshmallow import fields

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

class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])

    class Meta:
        fields = ('id', 'title', 'description', 'status', 'data_created', 'user')
        