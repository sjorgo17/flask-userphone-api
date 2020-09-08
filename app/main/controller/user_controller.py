from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import general_add, users, numberOfUsers

api = UserDto.api
_user = UserDto.user


@api.route('general_add')
@api.response(200, 'User successfully created.')
class AddUser(Resource):
    @api.doc('create_a_new_user')
    @api.expect(_user, validate=True)
    def post(self):
    
        """Creates a new user with phone numbers"""
        data = request.json
        return general_add(user_data=data)


@api.route('users/<page>')
@api.param('page', 'The page number')
class Users(Resource):
    @api.doc('get_all_users')
    def get(self, page):

        """Get all users according to specifications."""
        order=request.args.get('order',None)
        mod=request.args.get('mod',None)
        perPage=int(request.args.get('perPage',10))
        
        return users(page,order,mod,perPage)

@api.route('numberOfUsers')
class UserTotalNumber(Resource):
    @api.doc('number_of_all_users')
    def get(self):

        """Give total number of all registered users"""
        return numberOfUsers()