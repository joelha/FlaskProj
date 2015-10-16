from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import logout_user, login_required, login_user

import proj
from ..forms import UsernamePasswordForm
from ..models import User

mod = Blueprint('settings', __name__)

@mod.route('/settings')
@login_required
def settings():
	return render_template('settings/settings.html')

@mod.route('/settings-detail')
def detail():
	return render_template('settings/settings-detail.html')

@mod.route('/forecast')
def forecast():
	return render_template('settings/forecast.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():
	form = UsernamePasswordForm()

	if form.validate_on_submit():
		user = User('admin', 'pass')
		if user.password == form.password.data:
			login_user(user)
			print 'god pass'
			return redirect(url_for('.settings'))
		else:
			print 'bad pass'
			return redirect(url_for('.login'))
	print "didn't validate"
	return render_template('login.html', form=form)


@mod.route('/logout')
@login_required
def logout():
	logout_user()
	return render_template('home/home.html')