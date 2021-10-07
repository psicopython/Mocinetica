from flask import url_for

from typing import Any
from typing import Dict

from app.model import db


class Car(db.Model,dict):

    __tablename__ = "cars"
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(64), nullable=False )
    year = db.Column( db.String(64), nullable=False )
    brand = db.Column( db.String(64), nullable=False )
    engine = db.Column( db.String(64), nullable=False )
    gas_charge = db.Column( db.String(64), nullable=False )
    updated_at = db.Column( db.DateTime, nullable=True )
    created_at = db.Column( db.DateTime, nullable=False )
    

    def __init__(self, data: Dict[str, str] ) -> bool:
        for attrName, attrValue in data.items():
            if hasattr(self, attrName):
                setattr(self,attrName,attrValue)
                
    
    def getUrls(self) -> Dict[str,str]:
        return {
                "api": url_for("api.getCarByID",carID=self.id),
                "ui": url_for("ui.getCarByIDFull",carID=self.id, brand=self.brand, carName=self.name, carYear=self.year)
            }
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "brand": self.brand,
            "engine": self.engine,
            "gas_charge": self.gas_charge,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at) if self.updated_at else None,
            "urls": self.getUrls()
        }
