from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create an User table
    """
    # 表名
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    studentid = db.Column(db.String(60), index=True, unique=True)
    name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    # course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# 设置加载用户
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Group(db.Model):
    """
    Create a Group table
    """

    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users = db.relationship('User', backref='group',
                            lazy='dynamic')
    grouplinkcourses= db.relationship('GroupLinkCourse', backref='group',
                            lazy='dynamic')

    def __repr__(self):
        return '<Group: {}>'.format(self.name)


class Course(db.Model):
    """
    Create a Course table
    """

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))
    xueshi = db.Column(db.Integer)
    teacher = db.Column(db.String(60))

    grouplinkcourses = db.relationship('GroupLinkCourse', backref='course',
                                       lazy='dynamic')

    def __repr__(self):
        return '<Course: {}>'.format(self.name)



class GroupLinkCourse(db.Model):
    """
    Create a GroupLinkCourse table
    """

    __tablename__ = 'grouplinkcourses'

    id = db.Column(db.Integer, primary_key=True)
    shijian = db.Column(db.String(10), unique=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __repr__(self):
        return '<GroupLinkCourse: {}>'.format(self.name)
