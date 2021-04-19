from bottle import route, run, template, get, post,put, response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json
from models.users import Users
from uuid import UUID
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
# creation of a session
# https://towardsdatascience.com/a-guide-on-how-to-interact-between-python-and-databases-using-sqlalchemy-and-postgresql-a6d770723474
db = scoped_session(sessionmaker(bind=engine))
session = db()
# https://codeandlife.com/2014/12/07/sqlalchemy-results-to-json-the-easy-way/
# this one
# https://stackoverflow.com/a/10370224/2162857

#https://stackoverflow.com/questions/36588126/uuid-is-not-json-serializable


@get('/users')
@get('/users/<id>')
def get_users(id = None):
    response.content_type = 'application/json'
    if id != None:
        user = session.query(Users).get(id)
        return json.dumps(user.to_dict())
    else:
        user_list = session.query(Users).all()
        return json.dumps([r.to_dict() for r in user_list])



@post('/users')
def create_user():
    response.content_type = 'application/json'
    user = request.json
    new_user = Users(**user)
    session.add(new_user)
    session.commit()
    #https://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit/4202016#4202016
    session.refresh(new_user)
    return json.dumps(new_user.to_dict())


@put('/users')
def update_user():
    response.content_type = 'application/json'
    user = request.json
    new_user = Users(**user)
    session.add(new_user)
    session.commit()
    return json.dumps(new_user.to_dict())


run(host='localhost', port=8080,reloader=True, debug=True)