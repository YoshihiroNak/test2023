from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:1234@127.0.0.1:5432/trello'

# db = connect("postgresql://trello_dev:spameggs123@127.0.0.1:5432/trello", row_factory=dict_row, options="-c datestyle=ISO,YMD")

# @app.route('/cards')
# def all_cards():
#     card = db.execute("select * from cards where status = 'In Progress'").fetchall()
#     return card


db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

class Card(db.Model):
    __tablename__ = 'cards'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    status = db.Column(db.String(30))
    data_created = db.Column(db.Date())

    # def to_dict(self):
    #     return {'title': self.title, 'description': self.description, 'status': self.status, 'data_created': self.data_created}

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'data_created')
        

class User(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')


@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

@app.cli.command('db_seed')
def db_seed():
    users = [
        User(
            email="admin@spam.com",
            password=bcrypt.generate_password_hash("spinynorman123").decode('utf8'),
            is_admin=True
        ),
        User(
            name="john Cleese",
            email="cleese@spam.com",
            password=bcrypt.generate_password_hash("spam123").decode('utf8')
        )
    ]

    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create ERD',
            status = 'Done',
            data_created = date.today(),
        ),
        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement CRUD queries',
            status = 'Progres',
            data_created = date.today(),
        ),
        Card(
            title = 'Mashmallow',
            description = 'Stage 3 - Imprement JSONify of models',
            status = 'Progres',
            data_created = date.today(),
        ),
    ]

    db.session.add_all(users)
    db.session.add_all(cards)
    db.session.commit()

    print('Database seeded')

# @app.cli.command('all_cards')
# @app.route('/cards')
# def all_cards():
#     # select * from cards;
#     # stmt = db.select(Card).limit(2)
#     stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id < 3)).order_by(Card.title)
#     # cards = db.session.execute(stmt)
#     cards = db.session.scalars(stmt).all()
#     # card = db.session.scalar(stmt)
#     # print(list(cards))
#     # print(card)
#     # print(cards.all())
#     # for card in cards:
#     #     print(card.__dict__)
#     # return CardSchema(many=True).dumps(cards)
#     return CardSchema(many=True).dump(cards)

@app.route('/users/register', methods=['POST'])
def register():
    # Parse incoming POST body through the schema
    user_info = UserSchema(exclude=['id']).load(request.json)
    # Create a new user with the parsed data
    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
        name=user_info.get('name', '')
    )
    # Add and commit the new user to the database
    db.session.add(user)
    db.session.commit()

    # Return the new user
    return UserSchema(exclude=['password']).dump(user), 201



@app.route('/cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card) # .where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)
    # return [card.to_dict() for card in cards]



@app.route('/')
def index():
    return 'Hello World!!'

