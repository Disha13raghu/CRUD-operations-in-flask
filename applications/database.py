from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()
Base= declarative_base()
engine= None