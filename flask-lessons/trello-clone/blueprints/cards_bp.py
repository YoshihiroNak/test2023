from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.card import Card, CardSchema
from auth import authorize
from blueprints.comments_bp import comments_bp

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

cards_bp.register_blueprint(comments_bp)

#Get all cards
@cards_bp.route('/')
@jwt_required()
def all_cards():
    # select * from cards;
    stmt = db.select(Card) # .where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True, exclude=['user.cards']).dump(cards)
    # return [card.to_dict() for card in cards]

#Get one card
@cards_bp.route('/<int:id>')
@jwt_required()
def one_card(id):
    stmt = db.select(Card).filter_by(id=id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card:
        return CardSchema().dump(card)
    else:
        return {'error': 'Card not found'}, 404
    
#Create a new card
@cards_bp.route('/', methods=['POST'])
@jwt_required()
def create_card():
    card_info = CardSchema(exclude=["id", "data_created"]).load(request.json)
    card = Card(
        title = card_info['title'],
        description = card_info.get('description', ''),
        status = card_info.get('status', 'To Do'),
        user_id = get_jwt_identity()
    )
    db.session.add(card)
    db.session.commit()
    return CardSchema().dump(card), 201

# Update a card
@cards_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_card(id):
    card_info = CardSchema(exclude=["id", "data_created"]).load(request.json)
    stmt = db.select(Card).filter_by(id=id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card:
        authorize(card.user_id)
        card.title = card_info.get('title', card.title)
        card.description = card_info.get('description', card.description)
        card.status = card_info.get('status', card.status)
        db.session.commit()
        return CardSchema().dump(card)
    else:
        return {'error': 'Card not found'}, 404
    
# Delete a card
@cards_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_card(id):
    stmt = db.select(Card).filter_by(id=id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card:
        authorize(card.user_id)
        db.session.delete(card)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Card not found'}, 404
    
