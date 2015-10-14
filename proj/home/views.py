from flask import Blueprint, render_template

mod = Blueprint('home', __name__)

@mod.route('/')
@mod.route('/home')
def home():
	return render_template('home/home.html')