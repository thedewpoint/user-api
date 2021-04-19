from bottle import route, run, template, get, post, response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json
from models.users import Users
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
# creation of a session
# https://towardsdatascience.com/a-guide-on-how-to-interact-between-python-and-databases-using-sqlalchemy-and-postgresql-a6d770723474
db = scoped_session(sessionmaker(bind=engine))
session = db()
# https://codeandlife.com/2014/12/07/sqlalchemy-results-to-json-the-easy-way/
# this one
# https://stackoverflow.com/a/10370224/2162857

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
    session.add(Users(**user))
    session.commit()
    return json.dumps(user)


run(host='localhost', port=8080,reloader=True, debug=True)