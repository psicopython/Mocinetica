from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from typing import Dict

from app.model import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(64), nullable=False )
    email = db.Column( db.String(64), unique=True, nullable=False )
    password_hash = db.Column( db.String(128), nullable=False )

    @property
    def password(self):
        raise AttributeError("Attribute Password is not readble")
    
    @password.setter
    def password(self, passwd:str) -> None:
        self.password_hash = generate_password_hash(password=passwd)
    
    def checkPassword(self, passwd:str) -> bool:
        return check_password_hash(self.password_hash, passwd)
    
    def __init__(self, data: Dict[str, str] ) -> bool:
        self.name = data["name"]
        self.email = data["email"]
        self.password_hash = generate_password_hash(data["password"])
    
def validateEmail( email: str) -> bool:
    u = User.query.filter_by(email=email).first()
    if not u:
        tmp = email.split("@")
        if len(tmp) > 1:
            domi = tmp[0].split(".")
            if len(domi) > 1:
                return True
    return False