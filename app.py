from flask import Flask
from applications.config import developers
from applications.database import db



app= None

def setup():
	app= Flask(__name__, template_folder="D:/lab assignment 5/templates")
	app.config.from_object(developers)
	db.init_app(app)
	app.app_context().push()

setup()
from applications.controllers import *

if __name__ == '__main__':
	
	app.run(
	debug=True)
