from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from secretinfo import *


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = secret_key

@app.route("/")
def index():
    """ This is the route for the index page """
    return render_template("index.html")

@app.route("/application-form")
def application():
    """ This is the route for the survey page """
    JOBS = {"Software Engineer": "Software Engineer", "QA Engineer": "QA Engineer", "Product Manager": "Product Manager"}
    return render_template("application-form.html", jobs=JOBS)

@app.route("/application-success", methods=["POST"])
def app_success():
    """ This route captured the info from the user and display a cute message with it """
    
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    job = request.form['select']
    salary = request.form['quantity']

    # I try to prevent the case with shy users that don't type any salary

    try:
        salary_int = int(salary)
    except ValueError: 
        salary_int = 0.0

    return render_template("/application-response.html", 
                            firstname=firstname,
                            lastname=lastname,
                            job=job,
                            salary=salary_int,
                            )



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
