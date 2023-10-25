#!usr/bin/env python3

from faker import Faker
from app import app
from models import db, User

fake = Faker()

with app.app_context():

    def clear():
        print("Clearing server")
        User.query.delete()

    def seed_users(num_users):
        print("seeding users")
        for a in range(num_users):
            username = fake.user_name()
            email = fake.email()

            user =User(username = username, email = email)

            db.session.add(user)
        db.session.commit()


    if __name__ == "__main__":
        clear()
        num_users = 5
        seed_users(num_users)
        print(f'Seeded {num_users} users into the database.')