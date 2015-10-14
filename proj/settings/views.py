from flask import Blueprint, render_template

mod = Blueprint('settings', __name__)

@mod.route('/settings')
def settings():
	return render_template('settings/settings.html')

@mod.route('/settings-detail')
def detail():
	return render_template('settings/settings-detail.html')

@mod.route('/forecast')
def forecast():
	return render_template('settings/forecast.html')