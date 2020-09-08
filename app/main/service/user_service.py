import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.phonenumber import PhoneNumber

def general_add(user_data):
    
    #Create and add new user
    new_user=User(name=user_data['name'],surname=user_data['surname'])
    db.session.add(new_user)
    db.session.commit()

    numbers=user_data['numbers']
    number_objects=[]

    #Create the PhoneNumber objects associated with the user
    for number_data in numbers:
        new_number=PhoneNumber(uid=new_user.id,phoneNumber=number_data['phoneNumber'],type=number_data['type'])
        number_objects.append(new_number)

    #Add the phone numbers in the db
    db.session.add_all(number_objects)
    db.session.commit()

    response_object = {
        'success': True,
        'message': 'Successfully registered.'
        }

    return response_object, 200


def numberOfUsers():

    #Get total number of users.
    allUsers=User.query.count()
    return {'allUsers' : allUsers}


def users(page_num,order,mod,perPage):
    
    page=int(page_num)

    #Sort and paginate data according to parameters.
    if order=="name":
        user_list= User.query.order_by(User.name.desc() if mod=="desc" else User.name.asc()).paginate(per_page=perPage,page=page,error_out=True)
    
    elif order=="surname":     
        user_list= User.query.order_by(User.surname.desc() if mod=="desc" else User.surname.asc()).paginate(per_page=perPage,page=page,error_out=True)
     
    else:
        user_list= User.query.paginate(per_page=perPage,page=page,error_out=True)

    #Create list of users to store all the data
    users=[]

    for user in user_list.items:
        record={}
        record['id']=user.id
        record['name']=user.name
        record['surname']=user.surname
        record['numbers']=[]
        for number in user.numbers:
            record['numbers'].append({'id':number.id ,'phoneNumber':number.phoneNumber,'type':number.type})
        users.append(record)

    return {'users' : users}
