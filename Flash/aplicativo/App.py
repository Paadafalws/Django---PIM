from flask import Flask, redirect,render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import redirect



App = Flask(__name__)
App.secret_key="admin"

App.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
db = SQLAlchemy(App)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    funcao = db.Column(db.String(80), nullable=False)

def __init__(self,nome,funcao):
    self.nome = nome
    self.nome = nome

@App.route('/')
def index ():
    return render_template("index.html")

@App.route('/usuarios', methods=['POST'])
def dashbord():
    return redirect(url_for('dashbord.html'))




if __name__ == "__main__":
    App.run(debug=True)