# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "nishita" 
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home2():

    name = "father" 
    age = "47" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def home3():

    name = "mother" 
    age = "45" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friends")
def home4():

    name = "friend" 
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want
@app.route("/others")
def home5():

    name = "nishita" 
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
