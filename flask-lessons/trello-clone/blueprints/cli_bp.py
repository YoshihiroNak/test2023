from flask import Blueprint
from setup import db, bcrypt
from models.card import Card
from models.user import User
from datetime import date


db_commands = Blueprint('db' , __name__) 

@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

@db_commands.cli.command('seed')
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
