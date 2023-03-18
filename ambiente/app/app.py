from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class UserForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    submit = SubmitField('Submit')

@app.route('/')
def read():
    users = User.query.all()
    return render_template('read.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get(id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('read'))

if __name__ == '__main__':
    app.run(debug=True)
