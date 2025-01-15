from flask import Flask, render_template, redirect, url_for, flash,g,request,abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import os
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL",'sqlite:///models.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Base=declarative_base()


class Admin(db.Model):
    __tablename__="admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    password=db.Column(db.String(200),nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Model(db.Model):
    __tablename__='model'
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String, unique=True, nullable=False)
    height=db.Column(db.Integer, nullable=False)
    weight=db.Column(db.Integer, nullable=False)
    chest=db.Column(db.Integer, nullable=False)
    waist=db.Column(db.Integer, nullable=False)
    hips=db.Column(db.Integer, nullable=False)
    shoe_size=db.Column(db.Integer, nullable=False)
    trouser_length=db.Column(db.String, nullable=False)
    mobile_number=db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.model_name}>'

db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact_us")
def contact():
    return render_template("contact.html")

@app.route("/become_a_model")
def models():
    return render_template("becomeamodel.html")



@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/models")
def model():
    path = "static\\img\\model"
    models_name=[]
    path_list=[]
    obj = os.scandir(path=path)
    
    # List all files and directories in the model folder
    for entry in obj:
        if entry.is_dir():
            models_name.append(entry.name)#gets model name from the folder and adds its to the list of models
            image_path= os.listdir(path=entry.path)
            path_list.append(image_path[0])#appends the first image of the folder to the path list array
            
    return render_template("newmodel.html",model_list=models_name,image=path_list)


@app.route('/<name>')
def template(name):    
    word=name

    model= Model.query.filter_by(model_name=name).first()
    
    path= "static\\img\\model\\"
    new = path + word #get path for the specific model folder
    obj = os.scandir(path=new) #use the path for the model folder 
    image_path=[]
    for entry in obj: #this entry is for the specific model folder
        if entry.is_dir() or entry.is_file():
            # print(entry.name)#image name
            image_path.append(entry.name) 
    return render_template('template.html',model=word,image=image_path,model_details=model)

    
if __name__ == '__main__':
    app.run(debug=True)
    
