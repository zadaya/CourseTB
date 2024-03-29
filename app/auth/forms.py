from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """

    email = StringField("电子邮件", validators=[DataRequired(), Email()])
    studentid = StringField("学号", validators=[DataRequired()])
    name = StringField("姓名", validators=[DataRequired()])
    password = PasswordField(
        "密码", validators=[DataRequired(), EqualTo("confirm_password")]
    )
    confirm_password = PasswordField("确认密码")
    submit = SubmitField("注册")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("此电子邮件地址已注册")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("此学号已注册")


class LoginForm(FlaskForm):
    """
    Form for users to login
    """

    email = StringField("电子邮件", validators=[DataRequired(), Email()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("登陆")

