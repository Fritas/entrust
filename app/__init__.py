"""
    __init__ do módulo app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from socket import gethostbyname, gethostname

#app
app = Flask(__name__)

#database
db = SQLAlchemy
migrate = Migrate(app, db)

#server
server = Server(host='192.168.56.1', port=5000, use_debugger=True)
print('IP: ', gethostbyname(gethostname()))

#manager
manager = Manager(app)

#manager add command
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())



#controllers
from app.controllers import default
from app.controllers import error
