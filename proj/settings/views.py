from flask import Blueprint, render_template

mod = Blueprint('settings', __name__)

@mod.route('/settings')
def settings():
	return render_template('settings/settings.html')