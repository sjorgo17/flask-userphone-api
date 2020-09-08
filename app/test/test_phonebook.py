import unittest
import datetime
import json

from app.main import db
from app.main.model.user import User
from app.main.model.phonenumber import PhoneNumber 
from app.main.service.user_service import general_add,numberOfUsers,users
from app.test.base import BaseTestCase


#Helper methods for the development of integration tests

def register_new_user(self):
    return self.client.post(
        'general_add',
        data=json.dumps(dict(
            name='Stela',
            surname='Jorgo',
            numbers=[{'phoneNumber':'+123456','type':'Work'}]
        )),
        content_type='application/json'
    )

def register_invalid_user(self):
    return self.client.post(
        'general_add',
        data=json.dumps(dict(
            name='John',
            surname='Doe',
            numbers=[{'phoneNumber':'+m123','type':'Personal'}]
        )),
        content_type='application/json'
    )

def get_number_of_users(self):
    return self.client.get('numberOfUsers')

def get_users_ordered_by_name_desc(self):
    return self.client.get('users/1?order=name&mod=desc&perPage=10')

def get_users_ordered_by_surname_asc(self):
    return self.client.get('users/1?order=surname&mod=asc&perPage=1')


class TestUserModel(BaseTestCase):

    def test_number_of_users(self):    
        response=get_number_of_users(self)

        self.assertEqual(response.json['allUsers'],3)
        self.assert200(response)


    def test_register_user(self):

        #Test registering valid user
        response = register_new_user(self)
        response_in_json=response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_in_json['success'],True)

        #Test registering invalid user
        response = register_invalid_user(self)
        response_in_json=response.json

        self.assertEqual(response.status_code,400)
        self.assertTrue(response_in_json['errors'])


 
    def test_get_users(self):

        #Test ordering the users according to surname in asc order with perPage=1
        response=get_users_ordered_by_name_desc(self)
        response_in_json=response.json

        self.assertEqual(len(response_in_json['users']), 3)
        self.assertEqual(response_in_json['users'][0]['name'],'Zara')
        self.assertEqual(response_in_json['users'][2]['name'],'Ann')
        self.assertEqual(response.status_code,200)

        #Test ordering the users according to surname in asc order with perPage=1
        response=get_users_ordered_by_surname_asc(self)
        response_in_json=response.json

        self.assertEqual(len(response_in_json['users']), 1)
        self.assertEqual(response_in_json['users'][0]['name'],'Zara')
        self.assertEqual(response.status_code,200)
    

    def test_all_components(self):

        register_new_user(self)
        response_1=get_number_of_users(self)
        response_2=get_users_ordered_by_name_desc(self)

        self.assertEqual(response_1.json['allUsers'],4)
        self.assertEqual(len(response_2.json['users']), 4)
        self.assertEqual(response_2.json['users'][0]['name'],'Zara')

    #Unit testing

    def test_numberOfUsers(self):
        result=numberOfUsers()
        self.assertEqual(result['allUsers'],3)

    def test_general_add(self):
        user={'name':'Hanna','surname':'Smith','numbers':[{'phoneNumber':'111','type':'Work'}]}
        result=general_add(user_data=user)
        self.assertEqual(result[0]['success'],True)

    def test_users(self):
        result=users(1,'name','desc',10)
        users_data=result['users']
        self.assertEqual(len(users_data),3)
        self.assertEqual(users_data[0]['name'],'Zara')
        

if __name__ == '__main__':
    unittest.main()