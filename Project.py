from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators, SubmitField, IntegerField

app = Flask(__name__)
app.secret_key = "development key"
countries =                 [("Afghanistan","Afghanistan"),("Albania","Albania"),("Algeria","Algeria"),("Andorra","Andorra"),("Angola","Angola"),("Anguilla","Anguilla"),("Anguilla","Anguilla"),("Argentina","Argentina"),("Armenia","Armenia"),("Aruba","Aruba"),("Australia","Australia"),("Austria","Austria"),("Azerbaijan","Azerbaijan"),("Bahamas"
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
    password = StringField("Password : ",[validators.DataRequired("Please enter your password!")])
    submit = SubmitField("Submit")

class register_form(Form):
    username = StringField("User Name : ",[validators.DataRequired("Please enter a username!")])
    password = StringField("Password : ",[validators.DataRequired("Please enter a password!")])
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

@app.route("/", methods = ["POST", "GET"])
def main():
    loginform = login_form(request.form)


    if request.method == "GET":
        return render_template("main.html", loginform = loginform)

    elif request.method == "POST" and loginform.validate() == False :
            return render_template("main.html", loginform = loginform)

    elif request.method == "POST" and loginform.validate() == True:
            return render_template("home.htm")

    else :
        return render_template("home.htm")

@app.route("/login_register", methods = ['POST', "GET"])
def login_register():
    register = register_form(request.form)

    if request.method == "GET" :
        return render_template("login_register.html", register = register)

    elif request.method == "POST" and register.validate() == False:
        return render_template("login_register.html", register = register)

    elif request.method == "POST" and register.validate() == True:
        return render_template("home.htm")


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
