from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route('/home')
def home():
    return render_template('home.htm')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
