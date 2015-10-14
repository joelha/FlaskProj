from flask import Flask, render_template
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)

from home.views import mod as homeModule
app.register_blueprint(homeModule)

from settings.views import mod as settingsModule
app.register_blueprint(settingsModule)

from about.views import mod as aboutModule
app.register_blueprint(aboutModule)