from flask_testing import TestCase
from app.main import db
from app.main.model.user import User
from app.main.model.phonenumber import PhoneNumber 
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app
    
    #create and drop your tables with each test run to ensure clean tests
    def setUp(self):
        db.create_all()
        userslist=[
            User(name='Ann',surname='Leengi',numbers=[PhoneNumber(uid='1',phoneNumber='111',type='Work')]),
            User(name='Ben',surname='Wardiff',numbers=[PhoneNumber(uid='2',phoneNumber='222',type='Work')]),
            User(name='Zara',surname='Jorgo',numbers=[PhoneNumber(uid='3',phoneNumber='333',type='Personal'),PhoneNumber(uid='3',phoneNumber='444',type='Work')])
        ]
        db.session.add_all(userslist)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()