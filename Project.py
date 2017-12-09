from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/login_register")
def login_register():
    return render_template("login_register.html")

@app.route('/home', methods = ['POST'])
def home(username = "", password=""):
    if request.method == "POST" :
        username_ = request.form['login_username']
        password_ = request.form['login_password']
        if username_ == "user" and password_ == "pass" :
            return render_template("home.htm", username = username_ , password = password_)
        else :
            return '<script> alert("Wrong Login Credentials!"); window.location.href = "/";</script>'

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True)
