from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

db = SQLAlchemy()

class Model:
    
    def __init__(self, app: "Flask") -> None:
        db.init_app(app)
        app.db = db
        Migrate(app,app.db)

        from .tables.users import User
        # apartir daqui ele mapeia tds as outras tabelas