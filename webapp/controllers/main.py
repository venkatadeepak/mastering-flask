from flask import (render_template,
current_app,
Blueprint,
redirect,
url_for,
request,
flash,
session)
from webapp.forms import LoginForm, RegistrationForm 
from webapp.models import User, db
main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder = '../templates/main'
)

@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))

@main_blueprint.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html', form=form)

@main_blueprint.route('/logout', methods=['GET','POST'])
def logout():
    flash("You have been logged out", category="success")
    return redirect(url_for('.home'))

@main_blueprint.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login.", category='success')
        return redirect(url_for('.login'))

    return render_template('register.html', form=form)

