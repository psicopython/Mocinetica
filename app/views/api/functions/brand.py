from flask import request
from flask import jsonify
from flask import current_app as capp

from werkzeug.utils import secure_filename

from typing import Any

from datetime import datetime
from datetime import timezone

from app.model.tables.brands import Brand
from app.views.auth.functions.utils import loginRequired


class BrandResources:

    @classmethod
    def getBrand(cls, brandID, *args, **kwargs) -> Any:
        brand = Brand.query.filter_by(id=brandID).first()
        if isinstance(brand, Brand):
            return jsonify(brand.to_dict()), 200
        return jsonify({"message":"item not found"}), 404
    
    @classmethod
    def getBrands(cls, *args, **kwargs) -> Any:
        brands = Brand.query.all()
        
        return jsonify([ brand.to_dict() for brand in brands ]), 200

    @classmethod
    @loginRequired
    def setBrand(cls, *args, **kwargs) -> Any:
        """Adiciona uma montadora de Carros no DB"""
        data = request.form.to_dict() or request.json
        if data is None:
            return jsonify({"message": "request payload is invalid"}), 400
        
        for attrName, attrValue in data.items():
            if isinstance(attrValue, str):
                data[attrName] = attrValue.title()

        brand = Brand.query.filter_by(name=data["name"]).first()
        if isinstance(brand,Brand):
            return jsonify({"message": "brand name is not avaliable"}), 400

        brand = Brand(data)
        brand.created_at = datetime.now(timezone.utc)
        capp.db.session.add(brand)
        capp.db.session.commit()

        return jsonify(brand.to_dict()), 201


    @classmethod
    @loginRequired
    def updateBrand(cls, brandID, *args, **kwargs) -> Any:
        brandID = brandID["brandID"]
        data = request.form.to_dict() or request.json

        if data is None:
            return jsonify({"message": "brand name is required"}), 400
        
        for attrName, attrValue in data.items():
            if isinstance(attrValue, str):
                data[attrName] = attrValue.title()

        brand = Brand.query.filter_by(name=data["name"]).first()
        if isinstance(brand, Brand):
            return jsonify({"message": "brand with this name already exists"}), 200


        brand = Brand.query.filter_by(id=brandID).first()
        if isinstance(brand, Brand):
            for attrName, attrValue in data.items():
                if hasattr(brand, attrName):
                    setattr(brand, attrName, attrValue)
            capp.db.session.add(brand)
            capp.db.session.commit()
            return jsonify(brand.to_dict()), 200

        brand = Brand(data)
        brand.created_at = datetime.now(timezone.utc)
        capp.db.session.add(brand)
        capp.db.session.commit()
        return jsonify(brand.to_dict()), 201
    
    @classmethod
    @loginRequired
    def deleteBrand(cls, brandID, *args, **kwargs) -> Any:
        brandID = brandID["brandID"]
        brand = Brand.query.filter_by(id=brandID).first()
        if isinstance(brand,Brand):
            capp.db.session.delete(brand)
            capp.db.session.commit()
            return jsonify({}), 204
        return jsonify({"message":"item not found"}), 404