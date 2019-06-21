from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Group, Course, User


class GroupForm(FlaskForm):
    """
    Form for admin to add or edit a group
    """
    name = StringField('名称', validators=[DataRequired()])
    description = StringField('描述', validators=[DataRequired()])
    submit = SubmitField('提交')


class CourseForm(FlaskForm):
    """
    Form for admin to add or edit a course
    """
    name = StringField('名称', validators=[DataRequired()])
    description = StringField('描述', validators=[DataRequired()])
    xueshi = IntegerField('学时', validators=[DataRequired()])
    teacher = StringField('教师', validators=[DataRequired()])
    submit = SubmitField('提交')


class UserForm(FlaskForm):
    """
    Form for admin to assign departments and roles to user
    """
    studentid = StringField('StudentID', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    group = QuerySelectField(query_factory=lambda: Group.query.all(), get_label="name")

    submit = SubmitField('提交')
