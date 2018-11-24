"""
    __init__ of the main module
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from socket import gethostbyname, gethostname

#app
app = Flask(__name__)
app.config.from_object('config')

#database
db = SQLAlchemy
migrate = Migrate(app, db)

#server
endereco_ipv4 = gethostbyname(gethostname())
server = Server(host=endereco_ipv4, port=80)

#manager
manager = Manager(app)

#manager add command
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)



#controllers
from app.controllers import default
from app.controllers import error
