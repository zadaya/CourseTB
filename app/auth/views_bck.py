from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            name=form.name.data,
                            password=form.password.data)

        # 把员工信息写入数据看
        db.session.add(employee)
        db.session.commit()
        flash('注册成功，可以登录！')

        # 重定向到登陆页面
        return redirect(url_for('auth.login'))

    # 装载注册页面
    return render_template('auth/register.html', form=form, title='注册')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # 检查员工是否在数据库里并且密码是否正确
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            # 成功登陆
            login_user(employee)

            # 重定向到正确的工作台页面
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))

        # 登陆信息不正确
        else:
            flash('电子邮件地址或密码不正确！')

    # 重新加载登陆页面
    return render_template('auth/login.html', form=form, title='登录')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('成功注销！')

    # 重定向到登陆页面
    return redirect(url_for('auth.login'))
