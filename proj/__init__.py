from flask import Flask, render_template
from flask.ext.login import LoginManager
from .models import User

app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = '.login'

@lm.user_loader
def load_user(username):
	return User(username, 'pass')

from views.home import mod as homeModule
app.register_blueprint(homeModule)

from views.settings import mod as settingsModule
app.register_blueprint(settingsModule)

from views.about import mod as aboutModule
app.register_blueprint(aboutModule)