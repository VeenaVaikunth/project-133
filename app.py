# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "veena" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

app.run()
# define the route to father webpage
@app.route('/father')
def father():
    return 'father'
app.run()
# define the route to mother webpage
@app.route('/mother')
def mother():
    return 'mother'
app.run()
# define the route to friends webpage
@app.route('/friends')
def friends():
    return 'friends'
app.run()