from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web


__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user) ## 添加模型到数据库
        # db.session.commit() ## 提交到数据库
        return redirect(url_for('web.login'))
    # request.form
    return render_template('auth/register.html', form=form)
    pass


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next') #http://127.0.0.1:8080/login?next=%2Fmy%2Fgifts  取next后面的值，下面还需要对next做判断
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)



@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
