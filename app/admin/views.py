from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import UserForm, GroupForm, CourseForm
from .. import db
from ..models import User, Group, Course


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Group Views


@admin.route('/groups', methods=['GET', 'POST'])
@login_required
def list_groups():
    """
    List all groups
    """
    check_admin()

    groups = Group.query.all()

    return render_template('admin/groups/groups.html',
                           groups=groups, title="Groups")


@admin.route('/groups/add', methods=['GET', 'POST'])
@login_required
def add_group():
    """
    Add a group to the database
    """
    check_admin()

    add_group = True

    form = GroupForm()
    if form.validate_on_submit():
        group = Group(name=form.name.data,
                      description=form.description.data)
        try:
            # add group to the database
            db.session.add(group)
            db.session.commit()
            flash('成功添加一个班级')
        except:
            # in case group name already exists
            flash('错误: 此班级已存在')

        # redirect to groups page
        return redirect(url_for('admin.list_groups'))

    # load group template
    return render_template('admin/groups/group.html', action="Add",
                           add_group=add_group, form=form,
                           title="Add Group")


@admin.route('/groups/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_group(id):
    """
    Edit a group
    """
    check_admin()

    add_group = False

    group = Group.query.get_or_404(id)
    form = GroupForm(obj=group)
    if form.validate_on_submit():
        group.name = form.name.data
        group.description = form.description.data
        db.session.commit()
        flash('成功编辑一个班级信息')

        # redirect to the groups page
        return redirect(url_for('admin.list_groups'))

    form.description.data = group.description
    form.name.data = group.name
    return render_template('admin/groups/group.html', action="Edit",
                           add_group=add_group, form=form,
                           group=group, title="Edit Group")


@admin.route('/groups/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_group(id):
    """
    Delete a group from the database
    """
    check_admin()

    group = Group.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    flash('成功删除一个班级信息')

    # redirect to the groups page
    return redirect(url_for('admin.list_groups'))

    return render_template(title="Delete Group")


# Course Views


@admin.route('/courses')
@login_required
def list_courses():
    check_admin()
    """
    List all courses
    """
    courses = Course.query.all()
    return render_template('admin/courses/courses.html',
                           courses=courses, title='Courses')


@admin.route('/courses/add', methods=['GET', 'POST'])
@login_required
def add_course():
    """
    Add a course to the database
    """
    check_admin()

    add_course = True

    form = CourseForm()
    if form.validate_on_submit():
        course = Course(name=form.name.data,
                        description=form.description.data,
                        xueshi=form.xueshi.data,
                        teacher=form.teacher.data)

        try:
            # add course to the database
            db.session.add(course)
            db.session.commit()
            flash('成功添加一个新课程')
        except:
            # in case course name already exists
            flash('错误：此课程已存在')

        # redirect to the courses page
        return redirect(url_for('admin.list_courses'))

    # load course template
    return render_template('admin/courses/course.html', add_course=add_course,
                           form=form, title='Add Course')


@admin.route('/courses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_course(id):
    """
    Edit a course
    """
    check_admin()

    add_course = False

    course = Course.query.get_or_404(id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        course.name = form.name.data
        course.description = form.description.data
        course.xueshi = form.xueshi.data
        course.teacher = form.teacher.data
        db.session.add(course)
        db.session.commit()
        flash('成功编辑了一个课程信息')

        # redirect to the courses page
        return redirect(url_for('admin.list_courses'))

    form.description.data = course.description
    form.name.data = course.name
    return render_template('admin/courses/course.html', add_course=add_course,
                           form=form, title="Edit Course")


@admin.route('/courses/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_course(id):
    """
    Delete a course from the database
    """
    check_admin()

    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('成功删除一个课程信息')

    # redirect to the courses page
    return redirect(url_for('admin.list_courses'))

    return render_template(title="Delete Course")


# User Views

@admin.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    return render_template('admin/users/users.html',
                           users=users, title='Users')


@admin.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    """
    Assign a group and a course to an user
    """
    check_admin()

    user = User.query.get_or_404(id)

    # prevent admin from being assigned a group or course
    if user.is_admin:
        abort(403)

    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.studentid = form.studentid.data
        user.email = form.email.data
        user.group = form.group.data
        db.session.add(user)
        db.session.commit()
        flash('成功分配班级和配置课程')

        # redirect to the courses page
        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html',
                           user=user, form=form,
                           title='Assign User')
