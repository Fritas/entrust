"""
    __init__ do módulo app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_manager import Manager
from flask_migrate import Migrate, MigrateCommand

#app
app = Flask(__name__)

#database
db = SQLAlchemy
migrate = Migrate(app, db)

#manager
#manager = Manager(app)
#manager.add_command('db', MigrateCommand)

#controllers
from app.controllers import default
from app.controllers import error
