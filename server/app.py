from flask import Flask, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
api = Api(app)

db.init_app(app)

class Login(Resource):
    def get(self):
        pass

    def post(self):
        user = User.query.filter(User.username==request.get_json()["username"]).first()
        
        session["user_id"] = user.id
        
        return jsonify(user.to_dict())

api.add_resource(Login, "/login")
if __name__ == "__main__":
    app.run(port=5555)