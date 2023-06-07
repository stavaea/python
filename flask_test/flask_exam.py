# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/30 17:31
# @Author : waxberry
# @File : flask_exam.py
# @Software : PyCharm

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DateRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DateRequired()])
    email = StringField('Email', validators=[DateRequired()])
    submit = StringField('Submit')

@app.route('/', methods=['GET', 'POST'])

def index():
    form = UserForm()
    if form.validate_on_submit():
        # 将表单数据保存到数据库中
        user = User(name=form.name.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)