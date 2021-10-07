from typing import Any
from typing import Dict

from app.model import db


class Brand( db.Model ):
    __tablename__ = "brands"

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(64), unique=True, nullable=False )
    created_at = db.Column( db.String(64), nullable=False)

    def __init__( self, data: Dict[ str, Any ]) -> None:
        for attrName, attrValue in data.items():
            if hasattr( self, attrName ):
                setattr( self, attrName, attrValue)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at
        }
