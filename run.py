from flask import Flask, jsonify, request, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World! Lets go, test!"


# route for handling the login page logic
@app.route("/api/v1/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'dfraenk' or request.form['password'] != 'welkom01':
            error = 'Your username and/or password are incorrect!. Please try again.'
        else:
            return redirect(url_for('hello'))
    return render_template('login.html', error=error)



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
    wildcard_interface = "0.0.0.0" # Runs on all available interfaces
    app.run(debug=True, host=wildcard_interface)


print('App started')
