import os 

maindir= os.path.abspath(os.path.dirname(__file__))

class developers():
	sqldb= os.path.join(maindir,"../database")
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(sqldb,"database.sqlite3")