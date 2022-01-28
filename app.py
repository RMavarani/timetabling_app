from flask import render_template, Flask,request
from sqlalchemy import *



 
app = Flask(__name__)
engine= create_engine('sqlite:///data.db')
@app.route('/')
def index():
    
    return render_template("Base.html")

@app.route('/SignIn', methods=['POST', 'GET'])
def login (username,password):
  if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')

        user=User.query.filter_by(username=Username).first()
        return  render_template("SignIn.html")

@app.route('/SignUp')
def sign_up ():
        return render_template("SignUp.html")
if __name__ == '__main__':
      app.run(debug=True)