from flask import Flask, render_template, request, flash, redirect, url_for, session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators, SubmitField, IntegerField, PasswordField
from forms import Forms
from registerform import RegisterForm
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.secret_key = "development key"

#SocketIO
app.config['SECRET KEY'] = ''
socketio = SocketIO(app)

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('cred/digitalservices-d9e1c-firebase-adminsdk-3ms44-b4b21b1d32.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://digitalservices-d9e1c.firebaseio.com/'
})

root = db.reference()


countries = [("Afghanistan","Afghanistan"),("Albania","Albania"),("Algeria","Algeria"),("Andorra","Andorra"),("Angola","Angola"),("Anguilla","Anguilla"),("Anguilla","Anguilla"),("Argentina","Argentina"),("Armenia","Armenia"),("Aruba","Aruba"),("Australia","Australia"),("Austria","Austria"),("Azerbaijan","Azerbaijan"),("Bahamas"
		,"Bahamas"),("Bahrain","Bahrain"),("Bangladesh","Bangladesh"),("Barbados","Barbados"),("Belarus","Belarus"),("Belgium","Belgium"),("Belize","Belize"),("Benin","Benin"),("Bermuda","Bermuda"),("Bhutan","Bhutan"),("Bolivia","Bolivia"),("Bosnia Herzegovina","Bosnia Herzegovina"),("Botswana","Botswana"),("Brazil","Brazil"),("British Virgin Islands"
		,"British Virgin Islands"),("Brunei","Brunei"),("Bulgaria","Bulgaria"),("Burkina Faso","Burkina Faso"),("Burundi","Burundi"),("Cambodia","Cambodia"),("Cameroon","Cameroon"),("Canada","Canada"),("Cape Verde","Cape Verde"),("Cayman Islands","Cayman Islands"),("Chad","Chad"),("Chile","Chile"),("China","China"),("Colombia","Colombia"),("Congo","Congo"),("Cook Islands","Cook Islands"),("Costa Rica"
		,"Costa Rica"),("Cote D Ivoire","Cote D Ivoire"),("Croatia","Croatia"),("Cruise Ship","Cruise Ship"),("Cuba","Cuba"),("Cyprus","Cyprus"),("Czech Republic","Czech Republic"),("Denmark","Denmark"),("Djibouti","Djibouti"),("Dominica","Dominica"),("Dominican Republic","Dominican Republic"),("Ecuador","Ecuador"),("Egypt","Egypt"),("El Salvador","El Salvador"),("Equatorial Guinea","Equatorial Guinea")
		,("Estonia","Estonia"),("Ethiopia","Ethiopia"),("Falkland Islands","Falkland Islands"),("Faroe Islands","Faroe Islands"),("Fiji","Fiji"),("Finland","Finland"),("France","France"),("French Polynesia","French Polynesia"),("French West Indies","French West Indies"),("Gabon","Gabon"),("Gambia","Gambia"),("Georgia","Georgia"),("Germany","Germany"),("Ghana","Ghana")
		,("Gibraltar","Gibraltar"),("Greece","Greece"),("Greenland","Greenland"),("Grenada","Grenada"),("Guam","Guam"),("Guatemala","Guatemala"),("Guernsey","Guernsey"),("Guinea","Guinea"),("Guinea Bissau","Guinea Bissau"),("Guyana","Guyana"),("Haiti","Haiti"),("Honduras","Honduras"),("Hong Kong","Hong Kong"),("Hungary","Hungary"),("Iceland","Iceland"),("India","India")
		,("Indonesia","Indonesia"),("Iran","Iran"),("Iraq","Iraq"),("Ireland","Ireland"),("Isle of Man","Isle of Man"),("Israel","Israel"),("Italy","Italy"),("Japan","Japan"),("Jersey","Jersey"),("Jordan","Jordan"),("Kazakhstan","Kazakhstan"),("Kenya","Kenya"),("Kuwait","Kuwait"),("Kyrgyz Republic","Kyrgyz Republic"),("Laos","Laos"),("Latvia","Latvia")
		,("Lebanon","Lebanon"),("Lesotho","Lesotho"),("Liberia","Liberia"),("Libya","Libya"),("Liechtenstein","Liechtenstein"),("Lithuania","Lithuania"),("Luxembourg","Luxembourg"),("Macau","Macau"),("Macedonia","Macedonia"),("Madagascar","Madagascar"),("Malawi","Malawi"),("Malaysia","Malaysia"),("Maldives","Maldives"),("Mali","Mali"),("Malta","Malta"),("Mauritania","Mauritania")
		,("Mauritius","Mauritius"),("Mexico","Mexico"),("Moldova","Moldova"),("Monaco","Monaco"),("Mongolia","Mongolia"),("Montenegro","Montenegro"),("Montserrat","Montserrat"),("Morocco","Morocco"),("Mozambique","Mozambique"),("Namibia","Namibia"),("Nepal","Nepal"),("Netherlands","Netherlands"),("New Caledonia","New Caledonia")
		,("New Zealand","New Zealand"),("Nicaragua","Nicaragua"),("Niger","Niger"),("Nigeria","Nigeria"),("Norway","Norway"),("Oman","Oman"),("Pakistan","Pakistan"),("Palestine","Palestine"),("Panama","Panama"),("Papua New Guinea","Papua New Guinea"),("Paraguay","Paraguay"),("Peru","Peru"),("Philippines","Philippines"),("Poland","Poland"),("Portugal","Portugal")
		,("Puerto Rico","Puerto Rico"),("Qatar","Qatar"),("Reunion","Reunion"),("Romania","Romania"),("Russia","Russia"),("Rwanda","Rwanda"),("Samoa","Samoa"),("San Marino","San Marino"),("Saudi Arabia","Saudi Arabia"),("Senegal","Senegal"),("Serbia","Serbia"),("Seychelles","Seychelles")
		,("Sierra Leone","Sierra Leone"),("Singapore","Singapore"),("Slovakia","Slovakia"),("Slovenia","Slovenia"),("South Africa","South Africa"),("South Korea","South Korea"),("Spain","Spain"),("Sri Lanka","Sri Lanka"),("St Lucia","St Lucia"),("St Vincent","St Vincent"),("St. Lucia","St. Lucia"),("Sudan","Sudan")
		,("Suriname","Suriname"),("Swaziland","Swaziland"),("Sweden","Sweden"),("Switzerland","Switzerland"),("Syria","Syria"),("Taiwan","Taiwan"),("Tajikistan","Tajikistan"),("Tanzania","Tanzania"),("Thailand","Thailand"),("Timor L'Este","Timor L'Este"),("Togo","Tonga"),("Tunisia","Tunisia")
		,("Turkey","Turkey"),("Turkmenistan","Turkmenistan"),("Uganda","Uganda"),("Ukraine","Ukraine"),("United Arab Emirates","United Arab Emirates"),("United Kingdom","United Kingdom"),("United States","United States"),("Uruguay","Uruguay"),("Uzbekistan","Uzbekistan"),("Venezuela","Venezuela"),("Vietnam","Vietnam"),("Virgin Islands (US)","Virgin Islands (US)")
		,("Yemen","Yemen"),("Zambia","Zambia"),("Zimbabwe","Zimbabwe")]

class login_form(Form):
    username = StringField("Username : ",[validators.DataRequired("Please enter your username!")])
    password = PasswordField("Password : ",[validators.DataRequired("Please enter your password!")])
    submit = SubmitField("Submit")

class register_form(Form):
    username = StringField("User Name : ",[validators.DataRequired("Please enter a username!")])
    password = PasswordField("Password : ",[validators.DataRequired("Please enter a password!")])
    email = StringField("Email : ",[validators.DataRequired("Please enter your email!")])
    firstname = StringField("First Name : ",[validators.DataRequired("Please enter your First Name!")])
    lastname = StringField("Last Name : ",[validators.DataRequired("Please enter your Last Name")])
    age = IntegerField("Age : ",[validators.DataRequired("Please enter your age!")])
    country = SelectField(u"Country : ", choices=countries)
    highestqualification = StringField("Highest Qualification : ",[validators.DataRequired("Please enter your highest qualifications!")])
    workexperiences = StringField("Work Experiences : ",[validators.DataRequired("Please enter your work experiences!")])
    skillsets = StringField("Skillsets : ",[validators.DataRequired("Please enter your skillsets!")])
    awards = StringField("Awards : ",[validators.DataRequired("Please enter what awards you have received!")])
    bio = TextAreaField("Biography(Less than 500 words) : ")
    submit = SubmitField("Register")

class employer_register_form(Form):
    username = StringField("User Name : ", [validators.DataRequired("Please enter a username!")])
    password = PasswordField("Password : ", [validators.DataRequired("Please enter your password!")])
    company = StringField("Company Name : ", [validators.DataRequired("Please enter your company name!")])
    address = StringField("Company Address : ", [validators.DataRequired("Please enter your company address!")])
    email = StringField("Company Email : ", [validators.DataRequired("Please enter your company email!")])
    telno = IntegerField("Company Telephone : ", [validators.DataRequired("Please enter your company phone number!")])
    industry = StringField("Company Industry : ", [validators.DataRequired("Please enter your company industry!")])
    bio = TextAreaField("Company Biography(Tell us about your company) : ", [validators.DataRequired("Please enter your company biography")])
    submit = SubmitField("Register")

@app.route("/", methods = ["POST", "GET"])
def main():
    loginform = login_form(request.form)

    if request.method == "GET":
        return render_template("main.html", loginform = loginform)

    elif request.method == "POST" and loginform.validate() == False :
        return render_template("main.html", loginform = loginform)

    elif request.method == "POST" and loginform.validate() == True:
        name = loginform.username.data
        password = loginform.password.data
        logindata = root.child('userdata').get()
        for user in logindata :
            uniqueuser = logindata[user]
            if uniqueuser['username'] == name and uniqueuser['password'] == password :
                session['data'] = {
                    'username' : uniqueuser['username'],
                    'password': uniqueuser['password'],
                    'email' : uniqueuser['email'],
                    'age' : uniqueuser['age'],
                    'firstname' : uniqueuser['firstname'],
                    'lastname' : uniqueuser['lastname'],
                    'country' : uniqueuser['country'],
                    'highestqualification' : uniqueuser['highestqualification'],
                    'workexperiences' : uniqueuser['workexperiences'],
                    'skillsets' : uniqueuser['skillsets'],
                    'awards' : uniqueuser['awards'],
                    'bio' : uniqueuser['bio']
                }

                return redirect(url_for("login"))

        return '<script> alert("Wrong Login Credentials!"); window.location.href = "/";</script>'



@app.route("/login_register", methods = ['POST', "GET"])
def login_register():
    register = register_form(request.form)

    if request.method == "GET" :
        return render_template("login_register.html", register = register)

    elif request.method == "POST" and register.validate() == False:
        return render_template("login_register.html", register = register)

    elif request.method == "POST" and register.validate() == True:
        name = register.username.data
        password = register.password.data
        email = register.email.data
        firstname = register.firstname.data
        lastname = register.lastname.data
        age = register.age.data
        country = register.country.data
        highestqualification = register.highestqualification.data
        workexperiences = register.workexperiences.data
        skillsets = register.skillsets.data
        awards = register.awards.data
        bio = register.bio.data
        data = RegisterForm(name, password, email, firstname, lastname, age, country, highestqualification, workexperiences, skillsets, awards, bio)
        data_db = root.child('userdata')
        data_db.push({
            'username' : data.get_username(),
            'password' : data.get_password(),
            'email' : data.get_email(),
            'firstname' : data.get_firstname(),
            'lastname' : data.get_lastname(),
            'age' : data.get_age(),
            'country' : data.get_country(),
            'highestqualification' : data.get_highestqualification(),
            'workexperiences' : data.get_workexperiences(),
            'skillsets' : data.get_skillsets(),
            'awards' : data.get_awards(),
            'bio' : data.get_bio()
        })
        return redirect(url_for("login"))

@app.route("/login_register_employer", methods=["POST","GET"])
def login_register_employer():

    company = employer_register_form(request.form)

    if request.method == "GET" :
        return render_template("login_register_employer.html", company = company)

    elif request.method == "POST" and company.validate() == False :
        return render_template("login_register_employer.html", company = company)

    elif request.method == "POST" and company.validate() == True :
        return redirect(url_for("home"))

@app.route("/home")
def home() :
    return render_template('home.htm')

#Route to messenger
@app.route( '/messages' )
def hello():
  return render_template( 'ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )

@app.route('/account')
def accountsettings() :
    return render_template('AccountSettings.html')

@app.route('/help')
def help() :
    return render_template('help.html')

@app.route('/login')
def login() :
    session['loggedin'] = True
    return redirect(url_for('home'))

@app.route('/logout')
def logout() :
    session.pop('data', None)
    session['loggedin'] = False
    return redirect(url_for('main'))


@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
    socketio.run(app, debug = True)
