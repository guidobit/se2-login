import os
from imaplib import Response_code

from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask_marshmallow import Marshmallow
from marshmallow import pre_dump, pre_load, post_dump, post_load, fields
from bcrypt import hashpw, gensalt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy()
ma = Marshmallow()
db.init_app(app)
ma.init_app(app)


# Default responses
NOT_FOUND = Response("Niet gevonden", 404)
UNAUTHORIZED = Response("Verkeerde gegevens", 401)
SERVER_ERROR = Response("", 500)
SUCCESS = Response("", 200)


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String, nullable=True)

    def __str__(self):
        password = self.password
        return "<Account('%r', '%r', '%r')> (SAFETY REPRESENTATION)" % (self.name, self.email, replace_chars_with_asterisks(password))

    def hash_password(self):
        password = self.password
        salt = self.salt
        self.password = hashpw(password.encode('utf-8'), salt)

    def gen_salt(self):
        self.salt = gensalt(13)


class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account
        exclude=['salt', 'id']

    @pre_dump(pass_many=False)
    def post_load(self, data):
        #data.password = replace_chars_with_asterisks(data.password)
        return data


def replace_chars_with_asterisks(chars):
    return '*' * len(chars)




@app.route("/api/v3/register", methods=["GET", "POST"])
def registerv3():
    new_account= Account(
        email=request.values.get('email'),
        name=request.values.get('name'),
        password=request.values.get('password')
    )
    new_account.gen_salt()
    new_account.hash_password()
    try:
        db.session.add(new_account)
        db.session.commit()
    except Exception as err:
        print(err)
    print('New account created: ', new_account)
    new_account.password = replace_chars_with_asterisks(new_account.password)
    return AccountSchema().jsonify(new_account)


@app.route("/api/v3/login", methods=["GET", "POST"])
def loginv3():
    login_grant= Account(
        email=request.values.get('email'),
        name='',
        password=request.values.get('password')
    )
    account, account_json = None, None
    try:
        account = db.session.query(Account).first_or_404()
    except Exception as err:
        print(err)
    login = False
    if account.salt:
        login_grant.salt = account.salt
        login_grant.hash_password()
        if login_grant.password == account.password:
            login = True
            account.password = replace_chars_with_asterisks(account.password)
            account_json = AccountSchema().jsonify( account )
            return account_json
    return UNAUTHORIZED



@app.route("/", methods=["GET"])
def hello():
    return "Hello World! Lets go, test!"


@app.route("/api/v1/login", methods=["POST"])
def login():
    return "login api"


@app.route("/api/v1/register", methods=["POST","PUT"])
def register():
	error=None
	content = request.get_json()
	if request.method == 'PUT':
		  print (content['username'])
		  print (content['password'])
		  print (content['email'])
		  return "\nUser registration received for user %s\n" % content['username']
	else:
		error = 'Onjuiste registratie'
		#getest met curl -X PUT http://localhost:5000/api/v1/register -d "{\"username\":\"dcoomans\", \"password\":\"#W@chtw00rd23\",\"email\":\"dennis.coomans@hva.nl\"}" --header "Content-Type: application/json"

def valid_registration():
	error=None

def register_the_user():
	error=None

@app.route("/api/v1/logout", methods=["GET"])
def logout():
    return "logout api"


@app.route("/api/v1/validate/token", methods=["POST"])
def token():
    return "validate/token api"


@app.route("/api/v1/publickey", methods=["GET"])
def publickey():
    return "publickey api"


if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all(app=app)
            db.session.commit()
        except Exception as err:
            print(err)
    wildcard_interface = "0.0.0.0" # Runs on all available interfaces
    app.run(debug=True, host=wildcard_interface)


print('App started')
