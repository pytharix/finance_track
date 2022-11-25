from flask import Flask
from finance_track import routes

apps = Flask(__name__, template_folder='assets')
apps.secret_key = 'TinyJar Production'
apps.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root@127.0.0.1/tiny_jar'
apps.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
