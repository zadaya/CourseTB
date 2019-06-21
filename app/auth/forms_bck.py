from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """

    email = StringField("电子邮件", validators=[DataRequired(), Email()])
    username = StringField("用户名", validators=[DataRequired()])
    name = StringField("姓名", validators=[DataRequired()])
    password = PasswordField(
        "密码", validators=[DataRequired(), EqualTo("confirm_password")]
    )
    confirm_password = PasswordField("确认密码")
    submit = SubmitField("注册")

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError("此电子邮件地址已注册")

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError("此用户名已注册")


class LoginForm(FlaskForm):
    """
    Form for users to login
    """

    email = StringField("电子邮件", validators=[DataRequired(), Email()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("登陆")

