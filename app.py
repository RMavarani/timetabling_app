from flask import render_template, Flask
from database import *
 
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("Base.html")

@app.route('/SignIn')
def sign_in ():
        return  render_template("SignIn.html")

@app.route('/SignUp')
def sign_up ():
        return render_template("SignUp.html")
if __name__ == '__main__':
      app.run(debug=True)