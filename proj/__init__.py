from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from home.views import mod as homeModule
app.register_blueprint(homeModule)

from settings.views import mod as settingsModule
app.register_blueprint(settingsModule)