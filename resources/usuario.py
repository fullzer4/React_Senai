from flask_restful import Resource, reqparse
from models.usuario import UserModel

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message' : 'An error has ocurred when try to delete user.'}, 500
            return {'message' : 'User deleted.'}
        return {'message' : 'User not found'}, 404

    