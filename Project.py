from flask import Flask, render_template, request, flash, redirect, url_for, session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators, SubmitField, IntegerField, \
    PasswordField
from forms import Forms
from registerform import RegisterForm
from flask_socketio import SocketIO, emit
import datetime

app = Flask(__name__)
app.secret_key = "development key"

# SocketIO
app.config['SECRET KEY'] = ''
socketio = SocketIO(app)

import firebase_admin
from firebase_admin import credentials, db

# ZHENG TING's DATABASE
# cred = credentials.Certificate('cred/digitalservices-d9e1c-firebase-adminsdk-3ms44-b4b21b1d32.json')

# default_app = firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://digitalservices-d9e1c.firebaseio.com/'
# })

# JJ's DATABASE
cred = credentials.Certificate("cred/secondary-d4f0e-firebase-adminsdk-xa4rb-21094bbf76.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://secondary-d4f0e.firebaseio.com/'
})

root = db.reference()

countries = [("Afghanistan", "Afghanistan"), ("Albania", "Albania"), ("Algeria", "Algeria"), ("Andorra", "Andorra"),
             ("Angola", "Angola"), ("Anguilla", "Anguilla"), ("Anguilla", "Anguilla"), ("Argentina", "Argentina"),
             ("Armenia", "Armenia"), ("Aruba", "Aruba"), ("Australia", "Australia"), ("Austria", "Austria"),
             ("Azerbaijan", "Azerbaijan"), ("Bahamas"
                                            , "Bahamas"), ("Bahrain", "Bahrain"), ("Bangladesh", "Bangladesh"),
             ("Barbados", "Barbados"), ("Belarus", "Belarus"), ("Belgium", "Belgium"), ("Belize", "Belize"),
             ("Benin", "Benin"), ("Bermuda", "Bermuda"), ("Bhutan", "Bhutan"), ("Bolivia", "Bolivia"),
             ("Bosnia Herzegovina", "Bosnia Herzegovina"), ("Botswana", "Botswana"), ("Brazil", "Brazil"),
             ("British Virgin Islands"
              , "British Virgin Islands"), ("Brunei", "Brunei"), ("Bulgaria", "Bulgaria"),
             ("Burkina Faso", "Burkina Faso"), ("Burundi", "Burundi"), ("Cambodia", "Cambodia"),
             ("Cameroon", "Cameroon"), ("Canada", "Canada"), ("Cape Verde", "Cape Verde"),
             ("Cayman Islands", "Cayman Islands"), ("Chad", "Chad"), ("Chile", "Chile"), ("China", "China"),
             ("Colombia", "Colombia"), ("Congo", "Congo"), ("Cook Islands", "Cook Islands"), ("Costa Rica"
                                                                                              , "Costa Rica"),
             ("Cote D Ivoire", "Cote D Ivoire"), ("Croatia", "Croatia"), ("Cruise Ship", "Cruise Ship"),
             ("Cuba", "Cuba"), ("Cyprus", "Cyprus"), ("Czech Republic", "Czech Republic"), ("Denmark", "Denmark"),
             ("Djibouti", "Djibouti"), ("Dominica", "Dominica"), ("Dominican Republic", "Dominican Republic"),
             ("Ecuador", "Ecuador"), ("Egypt", "Egypt"), ("El Salvador", "El Salvador"),
             ("Equatorial Guinea", "Equatorial Guinea")
    , ("Estonia", "Estonia"), ("Ethiopia", "Ethiopia"), ("Falkland Islands", "Falkland Islands"),
             ("Faroe Islands", "Faroe Islands"), ("Fiji", "Fiji"), ("Finland", "Finland"), ("France", "France"),
             ("French Polynesia", "French Polynesia"), ("French West Indies", "French West Indies"), ("Gabon", "Gabon"),
             ("Gambia", "Gambia"), ("Georgia", "Georgia"), ("Germany", "Germany"), ("Ghana", "Ghana")
    , ("Gibraltar", "Gibraltar"), ("Greece", "Greece"), ("Greenland", "Greenland"), ("Grenada", "Grenada"),
             ("Guam", "Guam"), ("Guatemala", "Guatemala"), ("Guernsey", "Guernsey"), ("Guinea", "Guinea"),
             ("Guinea Bissau", "Guinea Bissau"), ("Guyana", "Guyana"), ("Haiti", "Haiti"), ("Honduras", "Honduras"),
             ("Hong Kong", "Hong Kong"), ("Hungary", "Hungary"), ("Iceland", "Iceland"), ("India", "India")
    , ("Indonesia", "Indonesia"), ("Iran", "Iran"), ("Iraq", "Iraq"), ("Ireland", "Ireland"),
             ("Isle of Man", "Isle of Man"), ("Israel", "Israel"), ("Italy", "Italy"), ("Japan", "Japan"),
             ("Jersey", "Jersey"), ("Jordan", "Jordan"), ("Kazakhstan", "Kazakhstan"), ("Kenya", "Kenya"),
             ("Kuwait", "Kuwait"), ("Kyrgyz Republic", "Kyrgyz Republic"), ("Laos", "Laos"), ("Latvia", "Latvia")
    , ("Lebanon", "Lebanon"), ("Lesotho", "Lesotho"), ("Liberia", "Liberia"), ("Libya", "Libya"),
             ("Liechtenstein", "Liechtenstein"), ("Lithuania", "Lithuania"), ("Luxembourg", "Luxembourg"),
             ("Macau", "Macau"), ("Macedonia", "Macedonia"), ("Madagascar", "Madagascar"), ("Malawi", "Malawi"),
             ("Malaysia", "Malaysia"), ("Maldives", "Maldives"), ("Mali", "Mali"), ("Malta", "Malta"),
             ("Mauritania", "Mauritania")
    , ("Mauritius", "Mauritius"), ("Mexico", "Mexico"), ("Moldova", "Moldova"), ("Monaco", "Monaco"),
             ("Mongolia", "Mongolia"), ("Montenegro", "Montenegro"), ("Montserrat", "Montserrat"),
             ("Morocco", "Morocco"), ("Mozambique", "Mozambique"), ("Namibia", "Namibia"), ("Nepal", "Nepal"),
             ("Netherlands", "Netherlands"), ("New Caledonia", "New Caledonia"), ("New Zealand", "New Zealand"),
             ("Nicaragua", "Nicaragua"), ("Niger", "Niger"), ("Nigeria", "Nigeria"), ("Norway", "Norway"),
             ("Oman", "Oman"), ("Pakistan", "Pakistan"), ("Palestine", "Palestine"), ("Panama", "Panama"),
             ("Papua New Guinea", "Papua New Guinea"), ("Paraguay", "Paraguay"), ("Peru", "Peru"),
             ("Philippines", "Philippines"), ("Poland", "Poland"), ("Portugal", "Portugal"),
             ("Puerto Rico", "Puerto Rico"), ("Qatar", "Qatar"), ("Reunion", "Reunion"), ("Romania", "Romania"),
             ("Russia", "Russia"), ("Rwanda", "Rwanda"), ("Samoa", "Samoa"), ("San Marino", "San Marino"),
             ("Saudi Arabia", "Saudi Arabia"), ("Senegal", "Senegal"), ("Serbia", "Serbia"),
             ("Seychelles", "Seychelles"), ("Sierra Leone", "Sierra Leone"), ("Singapore", "Singapore"),
             ("Slovakia", "Slovakia"), ("Slovenia", "Slovenia"), ("South Africa", "South Africa"),
             ("South Korea", "South Korea"), ("Spain", "Spain"), ("Sri Lanka", "Sri Lanka"), ("St Lucia", "St Lucia"),
             ("St Vincent", "St Vincent"), ("St. Lucia", "St. Lucia"), ("Sudan", "Sudan"), ("Suriname", "Suriname"),
             ("Swaziland", "Swaziland"), ("Sweden", "Sweden"), ("Switzerland", "Switzerland"), ("Syria", "Syria"),
             ("Taiwan", "Taiwan"), ("Tajikistan", "Tajikistan"), ("Tanzania", "Tanzania"), ("Thailand", "Thailand"),
             ("Timor L'Este", "Timor L'Este"), ("Togo", "Tonga"), ("Tunisia", "Tunisia"), ("Turkey", "Turkey"),
             ("Turkmenistan", "Turkmenistan"), ("Uganda", "Uganda"), ("Ukraine", "Ukraine"),
             ("United Arab Emirates", "United Arab Emirates"), ("United Kingdom", "United Kingdom"),
             ("United States", "United States"), ("Uruguay", "Uruguay"), ("Uzbekistan", "Uzbekistan"),
             ("Venezuela", "Venezuela"), ("Vietnam", "Vietnam"), ("Virgin Islands (US)", "Virgin Islands (US)"),
             ("Yemen", "Yemen"), ("Zambia", "Zambia"), ("Zimbabwe", "Zimbabwe")]

industries = [('Abortion Policy/Anti-Abortion', 'Abortion Policy/Anti-Abortion'),
              ('Abortion Policy/Pro-Abortion Rights', 'Abortion Policy/Pro-Abortion Rights'),
              ('Accountants', 'Accountants'), ('Advertising/Public Relations', 'Advertising/Public Relations'),
              ('Aerospace, Defense Contractors', 'Aerospace, Defense Contractors'), ('Agribusiness', 'Agribusiness'),
              ('Agricultural Services & Products', 'Agricultural Services & Products'), ('Agriculture', 'Agriculture'),
              ('Air Transport', 'Air Transport'), ('Air Transport Unions', 'Air Transport Unions'),
              ('Airlines', 'Airlines'), ('Alcoholic Beverages', 'Alcoholic Beverages'),
              ('Alternative Energy Production & Services', 'Alternative Energy Production & Services'),
              ('Architectural Services', 'Architectural Services'), ('Attorneys/Law Firms', 'Attorneys/Law Firms'),
              ('Auto Dealers', 'Auto Dealers'), ('Auto Dealers, Japanese', 'Auto Dealers, Japanese'),
              ('Auto Manufacturers', 'Auto Manufacturers'), ('Automotive', 'Automotive'),
              ('Banking, Mortgage', 'Banking, Mortgage'), ('Banks, Commercial', 'Banks, Commercial'),
              ('Banks, Savings & Loans', 'Banks, Savings & Loans'), ('Bars & Restaurants', 'Bars & Restaurants'),
              ('Beer, Wine & Liquor', 'Beer, Wine & Liquor'),
              ('Books, Magazines & Newspapers', 'Books, Magazines & Newspapers'),
              ('Broadcasters, Radio/TV', 'Broadcasters, Radio/TV'),
              ('Builders/General Contractors', 'Builders/General Contractors'),
              ('Builders/Residential', 'Builders/Residential'),
              ('Building Materials & Equipment', 'Building Materials & Equipment'),
              ('Building Trade Unions', 'Building Trade Unions'), ('Business Associations', 'Business Associations'),
              ('Business Services', 'Business Services'),
              ('Cable & Satellite TV Production & Distribution', 'Cable & Satellite TV Production & Distribution'),
              ('Candidate Committees', 'Candidate Committees'),
              ('Candidate Committees, Democratic', 'Candidate Committees, Democratic'),
              ('Candidate Committees, Republican', 'Candidate Committees, Republican'), ('Car Dealers', 'Car Dealers'),
              ('Car Dealers, Imports', 'Car Dealers, Imports'), ('Car Manufacturers', 'Car Manufacturers'),
              ('Casinos / Gambling', 'Casinos / Gambling'), ('Cattle Ranchers/Livestock', 'Cattle Ranchers/Livestock'),
              ('Chemical & Related Manufacturing', 'Chemical & Related Manufacturing'),
              ('Chiropractors', 'Chiropractors'),
              ('Civil Servants/Public Officials', 'Civil Servants/Public Officials'),
              ('Clergy & Religious Organizations', 'Clergy & Religious Organizations'),
              ('Clothing Manufacturing', 'Clothing Manufacturing'), ('Coal Mining', 'Coal Mining'),
              ('Colleges, Universities & Schools', 'Colleges, Universities & Schools'),
              ('Commercial Banks', 'Commercial Banks'),
              ('Commercial TV & Radio Stations', 'Commercial TV & Radio Stations'),
              ('Communications/Electronics', 'Communications/Electronics'), ('Computer Software', 'Computer Software'),
              ('Conservative/Republican', 'Conservative/Republican'), ('Construction', 'Construction'),
              ('Construction Services', 'Construction Services'), ('Construction Unions', 'Construction Unions'),
              ('Credit Unions', 'Credit Unions'),
              ('Crop Production & Basic Processing', 'Crop Production & Basic Processing'),
              ('Cruise Lines', 'Cruise Lines'), ('Cruise Ships & Lines', 'Cruise Ships & Lines'),
              ('Dairy', 'Dairy'), ('Defense', 'Defense'), ('Defense Aerospace', 'Defense Aerospace'),
              ('Defense Electronics', 'Defense Electronics'),
              ('Defense/Foreign Policy Advocates', 'Defense/Foreign Policy Advocates'),
              ('Democratic Candidate Committees', 'Democratic Candidate Committees'),
              ('Democratic Leadership PACs', 'Democratic Leadership PACs'),
              ('Democratic/Liberal', 'Democratic/Liberal'), ('Dentists', 'Dentists'),
              ('Doctors & Other Health Professionals', 'Doctors & Other Health Professionals'),
              ('Drug Manufacturers', 'Drug Manufacturers'), ('Education', 'Education'),
              ('Electric Utilities', 'Electric Utilities'),
              ('Electronics Manufacturing & Equipment', 'Electronics Manufacturing & Equipment'),
              ('Electronics, Defense Contractors', 'Electronics, Defense Contractors'),
              ('Energy & Natural Resources', 'Energy & Natural Resources'),
              ('Entertainment Industry', 'Entertainment Industry'), ('Environment', 'Environment'),
              ('Farm Bureaus', 'Farm Bureaus'), ('Farming', 'Farming'),
              ('Finance / Credit Companies', 'Finance / Credit Companies'),
              ('Finance, Insurance & Real Estate', 'Finance, Insurance & Real Estate'),
              ('Food & Beverage', 'Food & Beverage'), ('Food Processing & Sales', 'Food Processing & Sales'),
              ('Food Products Manufacturing', 'Food Products Manufacturing'), ('Food Stores', 'Food Stores'),
              ('For-profit Education', 'For-profit Education'), ('For-profit Prisons', 'For-profit Prisons'),
              ('Foreign & Defense Policy', 'Foreign & Defense Policy'),
              ('Forestry & Forest Products', 'Forestry & Forest Products'),
              ('Foundations, Philanthropists & Non-Profits', 'Foundations, Philanthropists & Non-Profits'),
              ('Funeral Services', 'Funeral Services'), ('Gambling & Casinos', 'Gambling & Casinos'),
              ('Gambling, Indian Casinos', 'Gambling, Indian Casinos'),
              ('Garbage Collection/Waste Management', 'Garbage Collection/Waste Management'),
              ('Gas & Oil', 'Gas & Oil'), ('Gay & Lesbian Rights & Issues', 'Gay & Lesbian Rights & Issues'),
              ('General Contractors', 'General Contractors'),
              ('Government Employee Unions', 'Government Employee Unions'),
              ('Government Employees', 'Government Employees'), ('Gun Control', 'Gun Control'),
              ('Gun Rights', 'Gun Rights'), ('Health', 'Health'),
              ('Health Professionals', 'Health Professionals'), ('Health Services/HMOs', 'Health Services/HMOs'),
              ('Hedge Funds', 'Hedge Funds'), ('HMOs & Health Care Services', 'HMOs & Health Care Services'),
              ('Home Builders', 'Home Builders'), ('Hospitals & Nursing Homes', 'Hospitals & Nursing Homes'),
              ('Hotels, Motels & Tourism', 'Hotels, Motels & Tourism'), ('Human Rights', 'Human Rights'),
              ('Ideological/Single-Issue', 'Ideological/Single-Issue'), ('Indian Gaming', 'Indian Gaming'),
              ('Industrial Unions', 'Industrial Unions'), ('Insurance', 'Insurance'), ('Internet', 'Internet'),
              ('Israel Policy', 'Israel Policy'), ('Labor', 'Labor'),
              ('Lawyers & Lobbyists', 'Lawyers & Lobbyists'), ('Lawyers / Law Firms', 'Lawyers / Law Firms'),
              ('Leadership PACs', 'Leadership PACs'), ('Liberal/Democratic', 'Liberal/Democratic'),
              ('Liquor, Wine & Beer', 'Liquor, Wine & Beer'), ('Livestock', 'Livestock'), ('Lobbyists', 'Lobbyists'),
              ('Lodging / Tourism', 'Lodging / Tourism'),
              ('Logging, Timber & Paper Mills', 'Logging, Timber & Paper Mills'),
              ('Manufacturing, Misc', 'Manufacturing, Misc'), ('Marine Transport', 'Marine Transport'),
              ('Meat processing & products', 'Meat processing & products'), ('Medical Supplies', 'Medical Supplies'),
              ('Mining', 'Mining'), ('Misc Business', 'Misc Business'), ('Misc Finance', 'Misc Finance'),
              ('Misc Manufacturing & Distributing', 'Misc Manufacturing & Distributing'),
              ('Misc Unions', 'Misc Unions'), ('Miscellaneous Defense', 'Miscellaneous Defense'),
              ('Miscellaneous Services', 'Miscellaneous Services'),
              ('Mortgage Bankers & Brokers', 'Mortgage Bankers & Brokers'),
              ('Motion Picture Production & Distribution', 'Motion Picture Production & Distribution'),
              ('Music Production', 'Music Production'), ('Natural Gas Pipelines', 'Natural Gas Pipelines'),
              ('Newspaper, Magazine & Book Publishing', 'Newspaper, Magazine & Book Publishing'),
              ('Non-profits, Foundations & Philanthropists', 'Non-profits, Foundations & Philanthropists'),
              ('Nurses', 'Nurses'), ('Nursing Homes/Hospitals', 'Nursing Homes/Hospitals'),
              ('Nutritional & Dietary Supplements', 'Nutritional & Dietary Supplements'),
              ('Oil & Gas', 'Oil & Gas'), ('Other', 'Other'), ('Payday Lenders', 'Payday Lenders'),
              ('Pharmaceutical Manufacturing', 'Pharmaceutical Manufacturing'),
              ('Pharmaceuticals / Health Products', 'Pharmaceuticals / Health Products'),
              ('Phone Companies', 'Phone Companies'),
              ('Physicians & Other Health Professionals', 'Physicians & Other Health Professionals'),
              ('Postal Unions', 'Postal Unions'), ('Poultry & Eggs', 'Poultry & Eggs'),
              ('Power Utilities', 'Power Utilities'), ('Printing & Publishing', 'Printing & Publishing'),
              ('Private Equity & Investment Firms', 'Private Equity & Investment Firms'), ('Pro-Israel', 'Pro-Israel'),
              ('Professional Sports, Sports Arenas & Related Equipment & Services',
               'Professional Sports, Sports Arenas & Related Equipment & Services'),
              ('Progressive/Democratic', 'Progressive/Democratic'), ('Public Employees', 'Public Employees'),
              ('Public Sector Unions', 'Public Sector Unions'), ('Publishing & Printing', 'Publishing & Printing'),
              ('Radio/TV Stations', 'Radio/TV Stations'), ('Railroads', 'Railroads'),
              ('Real Estate', 'Real Estate'), ('Record Companies/Singers', 'Record Companies/Singers'),
              ('Recorded Music & Music Production', 'Recorded Music & Music Production'),
              ('Recreation / Live Entertainment', 'Recreation / Live Entertainment'),
              ('Religious Organizations/Clergy', 'Religious Organizations/Clergy'),
              ('Republican Candidate Committees', 'Republican Candidate Committees'),
              ('Republican Leadership PACs', 'Republican Leadership PACs'),
              ('Republican/Conservative', 'Republican/Conservative'),
              ('Residential Construction', 'Residential Construction'),
              ('Restaurants & Drinking Establishments', 'Restaurants & Drinking Establishments'),
              ('Retail Sales', 'Retail Sales'), ('Retired', 'Retired'),
              ('Savings & Loans', 'Savings & Loans'), ('Schools/Education', 'Schools/Education'),
              ('Sea Transport', 'Sea Transport'), ('Securities & Investment', 'Securities & Investment'),
              ('Special Trade Contractors', 'Special Trade Contractors'),
              ('Sports, Professional', 'Sports, Professional'), ('Steel Production', 'Steel Production'),
              ('Stock Brokers/Investment Industry', 'Stock Brokers/Investment Industry'),
              ('Student Loan Companies', 'Student Loan Companies'),
              ('Sugar Cane & Sugar Beets', 'Sugar Cane & Sugar Beets'),
              ('Teachers Unions', 'Teachers Unions'), ('Teachers/Education', 'Teachers/Education'),
              ('Telecom Services & Equipment', 'Telecom Services & Equipment'),
              ('Telephone Utilities', 'Telephone Utilities'), ('Textiles', 'Textiles'),
              ('Timber, Logging & Paper Mills', 'Timber, Logging & Paper Mills'), ('Tobacco', 'Tobacco'),
              ('Transportation', 'Transportation'), ('Transportation Unions', 'Transportation Unions'),
              ('Trash Collection/Waste Management', 'Trash Collection/Waste Management'), ('Trucking', 'Trucking'),
              ('TV / Movies / Music', 'TV / Movies / Music'), ('TV Production', 'TV Production'),
              ('Unions', 'Unions'), ('Unions, Airline', 'Unions, Airline'),
              ('Unions, Building Trades', 'Unions, Building Trades'), ('Unions, Industrial', 'Unions, Industrial'),
              ('Unions, Misc', 'Unions, Misc'), ('Unions, Public Sector', 'Unions, Public Sector'),
              ('Unions, Teacher', 'Unions, Teacher'), ('Unions, Transportation', 'Unions, Transportation'),
              ('Universities, Colleges & Schools', 'Universities, Colleges & Schools'),
              ('Vegetables & Fruits', 'Vegetables & Fruits'), ('Venture Capital', 'Venture Capital'),
              ('Waste Management', 'Waste Management'), ('Wine, Beer & Liquor', 'Wine, Beer & Liquor'),
              ("Women's Issues", "Women's Issues")]


class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)


class login_form(Form):
    username = StringField("Username : ", [validators.DataRequired("Please enter your username!")])
    password = PasswordField("Password : ", [validators.DataRequired("Please enter your password!")])
    submit = SubmitField("Submit")


class register_form(Form):
    username = StringField("User Name : ", [validators.DataRequired("Please enter a username!")])
    password = PasswordField("Password : ", [validators.DataRequired("Please enter a password!")])
    email = StringField("Email : ", [validators.DataRequired("Please enter your email!")])
    firstname = StringField("First Name : ", [validators.DataRequired("Please enter your First Name!")])
    lastname = StringField("Last Name : ", [validators.DataRequired("Please enter your Last Name")])
    age = IntegerField("Age : ", [validators.DataRequired("Please enter your age!")])
    country = SelectField(u"Country : ", choices=countries)
    highestqualification = StringField("Highest Qualification : ",
                                       [validators.DataRequired("Please enter your highest qualifications!")])
    workexperiences = StringField("Work Experiences : ",
                                  [validators.DataRequired("Please enter your work experiences!")])
    skillsets = StringField("Skillsets : ", [validators.DataRequired("Please enter your skillsets!")])
    awards = StringField("Awards : ", [validators.DataRequired("Please enter what awards you have received!")])
    bio = TextAreaField("Biography(Less than 500 words) : ")
    submit = SubmitField("Register")


class employer_register_form(Form):
    username = StringField("User Name : ", [validators.DataRequired("Please enter a username!")])
    password = PasswordField("Password : ", [validators.DataRequired("Please enter your password!")])
    company = StringField("Company Name : ", [validators.DataRequired("Please enter your company name!")])
    address = StringField("Company Address : ", [validators.DataRequired("Please enter your company address!")])
    email = StringField("Company Email : ", [validators.DataRequired("Please enter your company email!")])
    telno = IntegerField("Company Telephone : ", [validators.DataRequired("Please enter your company phone number!")])
    industry = SelectField("Company Industry : ", choices=industries)
    bio = TextAreaField("Company Biography(Tell us about your company) : ",
                        [validators.DataRequired("Please enter your company biography")])
    submit = SubmitField("Register")


class create_job_posting(Form):
    job_title = StringField("Job Title : ", [validators.DataRequired("Please enter job title")])
    salary = IntegerField("Salary (Per Month) : ", [validators.DataRequired("Please enter salary")])
    career_level = SelectField("Career Level : ", choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    qualification = SelectField("Qualification : ", choices=[("Primary Qualification", "Primary Qualification"),
                                                             ("Lower Secondary", "Lower Secondary"),
                                                             ("Secondary Qualification", "Secondary Qualification"),
                                                             ("ITE Nitec / Higher Nitec", "ITE Nitec / Higher Nitec"),
                                                             ("Polytechnic Diploma", "Polytechnic Diploma"), (
                                                                 "Professional Qualification",
                                                                 "Professional Qualification"),
                                                             ("Bachelor's or Equivalent", "Bachelor's or Equivalent"),
                                                             ("Postgraduate Diploma", "Postgraduate Diploma"),
                                                             ("Master's and Doctorate", "Master's and Doctorate")])
    employment_type = SelectField("Employment Type : ",
                                  choices=[("Contract Full Time", "Contract Full Time"), ("Full Time", "Full Time"),
                                           ("Part Time", "Part Time"), ("Intern", "Intern")])
    employment_type_duration = StringField("Contract Time (Months) : ",
                                           [RequiredIf(employment_type="Contract Full Time")])
    lat = StringField("Latitude : ", [validators.DataRequired("Please click on the map!")])
    lng = StringField("Longitude : ")
    location = StringField("Location : ")
    job_des = TextAreaField("Job Description : ",
                            [validators.DataRequired("Please enter the description for the above mentioned job")])
    submit = SubmitField("Create Posting")


@app.route("/", methods=["POST", "GET"])
def main():
    loginform = login_form(request.form)

    if request.method == "GET":
        return render_template("main.html", loginform=loginform)

    elif request.method == "POST" and loginform.validate() == False:
        return render_template("main.html", loginform=loginform)

    elif request.method == "POST" and loginform.validate() == True:
        name = loginform.username.data
        password = loginform.password.data
        logindata = root.child('userdata').get()
        for user in logindata:
            uniqueuser = logindata[user]
            if uniqueuser['username'] == name and uniqueuser['password'] == password:
                if uniqueuser['status'] == "user":
                    session['data'] = {
                        'username': uniqueuser['username'],
                        'password': uniqueuser['password'],
                        'email': uniqueuser['email'],
                        'age': uniqueuser['age'],
                        'firstname': uniqueuser['firstname'],
                        'lastname': uniqueuser['lastname'],
                        'country': uniqueuser['country'],
                        'highestqualification': uniqueuser['highestqualification'],
                        'workexperiences': uniqueuser['workexperiences'],
                        'skillsets': uniqueuser['skillsets'],
                        'awards': uniqueuser['awards'],
                        'bio': uniqueuser['bio'],
                        'status': "user"
                    }
                else:
                    session['data'] = {
                        'username': uniqueuser['username'],
                        'password': uniqueuser['password'],
                        "company_name": uniqueuser['company_name'],
                        'email': uniqueuser['email'],
                        "telno": uniqueuser['telno'],
                        "address": uniqueuser['address'],
                        "industry": uniqueuser['industry'],
                        'bio': uniqueuser['bio'],
                        'status': "employer",
                        "notifications": uniqueuser["notifications"],
                        "applications": uniqueuser["applications"]
                    }

                return redirect(url_for("login"))

        return '<script> alert("Wrong Login Credentials!"); window.location.href = "/";</script>'


@app.route("/login_register", methods=['POST', "GET"])
def login_register():
    register = register_form(request.form)

    if request.method == "GET":
        return render_template("login_register.html", register=register)

    elif request.method == "POST" and register.validate() == False:
        return render_template("login_register.html", register=register)

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
        data = RegisterForm(name, password, email, firstname, lastname, age, country, highestqualification,
                            workexperiences, skillsets, awards, bio)
        session['data'] = {
            'username': name,
            'password': password,
            'email': email,
            'age': age,
            'firstname': firstname,
            'lastname': lastname,
            'country': country,
            'highestqualification': highestqualification,
            'workexperiences': workexperiences,
            'skillsets': skillsets,
            'awards': awards,
            'bio': bio,
            "status": "user"
        }
        data_db = root.child('userdata')
        data_db.push({
            'username': data.get_username(),
            'password': data.get_password(),
            'email': data.get_email(),
            'firstname': data.get_firstname(),
            'lastname': data.get_lastname(),
            'age': data.get_age(),
            'country': data.get_country(),
            'highestqualification': data.get_highestqualification(),
            'workexperiences': data.get_workexperiences(),
            'skillsets': data.get_skillsets(),
            'awards': data.get_awards(),
            'bio': data.get_bio(),
            "status": "user"
        })
        return redirect(url_for("login"))


@app.route("/login_register_employer", methods=["POST", "GET"])
def login_register_employer():
    company = employer_register_form(request.form)

    if request.method == "GET":
        return render_template("login_register_employer.html", company=company)

    elif request.method == "POST" and company.validate() == False:
        return render_template("login_register_employer.html", company=company)

    elif request.method == "POST" and company.validate() == True:
        username = company.username.data
        password = company.password.data
        company_name = company.company.data
        email = company.email.data
        telno = company.telno.data
        address = company.address.data
        industry = company.industry.data
        bio = company.bio.data

        session['data'] = {
            'username': username,
            'password': password,
            "company_name": company_name,
            'email': email,
            "telno": telno,
            "address": address,
            "industry": industry,
            'bio': bio,
            "status": "employer",
            "notifications": 0,
            "applicants": ''
        }

        data_db = root.child("userdata")
        data_db.push({
            "username": username,
            "password": password,
            "company_name": company_name,
            "email": email,
            "telno": telno,
            "address": address,
            "industry": industry,
            "bio": bio,
            "status": "employer",
            'notifications': 0,
            'applicants': ""
        })
        return redirect(url_for("login"))


@app.route("/home")
def home():
    try :
        notification = []
        for i in session['data']['applications'].split(","):
            if i == "":
                continue
            else:
                format_1 = i.split(":")
                jobpost = root.child("jobposts/" + format_1[1]).get()
                job_title = jobpost["job_title"]
                format_1.append(job_title)
                notification.append(format_1)
        return render_template('home.htm', notification=notification)
    except :
        return render_template("home.htm")


@app.route("/search_job")
def search_job():
    jobs = {}
    job = root.child("jobposts").get()
    reverse = sorted(job, reverse=True)
    for i in reverse:
        jobs[i] = job[i]
    print(root.child("userdata").get())
    return render_template("search_jobs.html", jobs=jobs)


@app.route("/create_job", methods=["GET", "POST"])
def create_job():
    create_form = create_job_posting(request.form)

    if request.method == "GET":
        return render_template("create_job.html", form=create_form)

    elif request.method == "POST" and create_form.validate() == False:
        return render_template("create_job.html", form=create_form)

    elif request.method == "POST" and create_form.validate() == True:
        # job details
        job_title = create_form.job_title.data
        salary = create_form.salary.data
        career = create_form.career_level.data
        qualification = create_form.qualification.data
        employment_type = create_form.employment_type.data
        contract_time = create_form.employment_type_duration.data
        latitude = create_form.lat.data
        longtitude = create_form.lng.data
        location = create_form.location.data
        job_description = create_form.job_des.data
        time = str(datetime.date.today())

        # employer details
        company_name = session["data"]["company_name"]
        company_email = session["data"]["email"]
        company_tel = session["data"]["telno"]
        company_address = session["data"]["address"]
        company_industry = session["data"]["industry"]
        company_bio = session["data"]["bio"]

        data_db = root.child('jobposts')
        data_db.push({
            'job_title': job_title,
            'salary': salary,
            'career': career,
            'qualification': qualification,
            'employment_type': employment_type,
            'contract_time': contract_time,
            'lat': latitude,
            'lng': longtitude,
            'location': location,
            'job_dec': job_description,
            'date': time,
            'company_name': company_name,
            'company_email': company_email,
            'company_tel': company_tel,
            'company_address': company_address,
            'company_industry': company_industry,
            'company_bio': company_bio
        })
        return '<script> alert("Successfully Posted, Returning to home now!"); window.location.href = "home";</script>'


@app.route('/edit_posts', methods=["GET", "POST"])
def edit_posts():
    jobs = {}
    job = root.child("jobposts").get()
    reverse = sorted(job, reverse=True)
    for i in reverse:
        jobs[i] = job[i]
    return render_template("edit_posts.html", jobs=jobs)


@app.route('/edit_post<post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    create_form = create_job_posting(request.form)
    if request.method == "GET":

        job_post = root.child('jobposts/' + post_id).get()
        create_form.job_title.data = job_post["job_title"]
        create_form.salary.data = job_post["salary"]
        create_form.career_level.data = job_post["career"]
        create_form.qualification.data = job_post["qualification"]
        create_form.employment_type.data = job_post["employment_type"]
        create_form.employment_type_duration.data = job_post["contract_time"]
        create_form.lat.data = job_post["lat"]
        create_form.lng.data = job_post["lng"]
        create_form.location.data = job_post["location"]
        create_form.job_des.data = job_post["job_dec"]
        return render_template('edit_post.html', post_id=post_id, job=job_post, form=create_form)

    elif request.method == "POST" and create_form.validate() == False:
        return render_template('edit_post.html', form=create_form)

    elif request.method == "POST" and create_form.validate() == True:
        job_title = create_form.job_title.data
        salary = create_form.salary.data
        career = create_form.career_level.data
        qualification = create_form.qualification.data
        employment_type = create_form.employment_type.data
        contract_time = create_form.employment_type_duration.data
        latitude = create_form.lat.data
        longtitude = create_form.lng.data
        location = create_form.location.data
        job_description = create_form.job_des.data
        time = str(datetime.date.today())

        company_name = session["data"]["company_name"]
        company_email = session["data"]["email"]
        company_tel = session["data"]["telno"]
        company_address = session["data"]["address"]
        company_industry = session["data"]["industry"]
        company_bio = session["data"]["bio"]

        job_post = root.child("jobposts/" + post_id)
        job_post.set({
            'job_title': job_title,
            'salary': salary,
            'career': career,
            'qualification': qualification,
            'employment_type': employment_type,
            'contract_time': contract_time,
            'lat': latitude,
            'lng': longtitude,
            'location': location,
            'job_dec': job_description,
            'date': time,
            'company_name': company_name,
            'company_email': company_email,
            'company_tel': company_tel,
            'company_address': company_address,
            'company_industry': company_industry,
            'company_bio': company_bio
        })

        return redirect(url_for("edit_posts"))


@app.route('/delete_post<post_id>')
def delete_post(post_id):
    post = root.child("jobposts/" + post_id)
    post.delete()
    return redirect(url_for("edit_posts"))


@app.route('/apply_job<post_id>')
def apply_job(post_id):
    company_userdata = ""
    find_company = root.child('jobposts/' + post_id).get()
    company_name = find_company["company_name"]
    find_company_userdata = root.child('userdata').get()
    for i in find_company_userdata:
        try:
            if find_company_userdata[i]["company_name"] == company_name:
                company_userdata = i
        except:
            continue
    company_db = root.child('userdata/' + company_userdata)
    company_userdata = root.child('userdata/' + company_userdata).get()
    applicant = session['data']['username']
    current_notifications = company_userdata["notifications"]
    current_applicants = company_userdata["applications"]
    if current_applicants == "":
        applicant = "," + applicant
    company_db.update({
        'notifications': current_notifications + 1,
        'applications': current_applicants + applicant + ":" + post_id + ","
    })
    return redirect("home")


@app.route('/show_application<applicant><job>')
def show_application(applicant,job):
    applicant = applicant+job
    form = register_form()
    form2 = create_job_posting()
    applicant_ = applicant.split("-")
    applicant_[1] = "-" + applicant_[1]
    find_applicant = root.child("userdata").get()
    for i in find_applicant :
        try :
            if find_applicant[i]["username"] == applicant_[0] :
                print(find_applicant[i]["username"])
                applicant = i
        except :
            continue
    #firstform
    get_details = root.child("userdata/" + applicant).get()
    form.firstname.data = get_details["firstname"]
    form.lastname.data = get_details["lastname"]
    form.age.data = get_details["age"]
    form.awards.data = get_details['awards']
    form.bio.data = get_details['bio']
    form.email.data = get_details['email']
    form.highestqualification.data = get_details['highestqualification']
    form.workexperiences.data = get_details['workexperiences']
    form.skillsets.data = get_details['skillsets']
    form.country.data = get_details['country']

    #secondform
    get_details2 = root.child("jobposts/" + applicant_[1]).get()
    form2.job_title.data = get_details2["job_title"]
    form2.career_level.data = get_details2["career"]
    form2.salary.data = get_details2["salary"]
    form2.qualification.data = get_details2["qualification"]
    form2.location.data = get_details2["location"]
    form2.lng.data = get_details2["lng"]
    form2.lat.data = get_details2["lat"]
    form2.job_des.data = get_details2["job_dec"]
    form2.employment_type.data = get_details2["employment_type"]
    form2.employment_type_duration.data = get_details2["contract_time"]
    return render_template("show_applicant.html", form = form,form2 = form2 ,user = get_details["firstname"])


# Route to messenger
@app.route('/messages')
def hello():
    return render_template('ChatApp.html')


def messageRecived():
    print('message was received!!!')


@app.route('/account')
def accountsettings():
    return render_template('AccountSettings.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/login')
def login():
    session['loggedin'] = True
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('data', None)
    session['loggedin'] = False
    return redirect(url_for('main'))


@socketio.on('my event')
def handle_my_custom_event(json):
    # store to database
    print('recived my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecived())


if __name__ == '__main__':
    socketio.run(app, debug=True)

# needed to refresh upload
