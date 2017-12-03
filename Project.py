from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
