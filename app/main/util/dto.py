from flask_restplus import Namespace, fields

class UserDto:

    api = Namespace('user', description='user related operations')

    phonenumber = api.model ('phone',{
        'phoneNumber':fields.String(required=True, pattern='^[0-9*#+-]+$'),
        'type':fields.String(required=True, enum=['Work','Personal'])
    })

    user = api.model('user', {
        'name': fields.String(required=True, pattern='^(?!\s*$).+', description='user name'),
        'surname': fields.String(required=True, pattern='^(?!\s*$).+', description='user surname'),
        'numbers': fields.List(fields.Nested(phonenumber))
    })
