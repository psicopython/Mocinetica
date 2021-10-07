from flask import jsonify
from flask import request
from flask import current_app as capp

from typing import Any

from datetime import datetime
from datetime import timezone

from app.views.auth.functions.utils import loginRequired

from app.model.tables.cars import Car



class CarResources:

    @classmethod
    # rota -> /api/cars/Fiat
    def getCars(cls, brand, *args, **kwargs) -> Any:
        cars = [car.to_dict() for car in Car.query.filter_by(brand=brand.title()).all()]
        count = len(cars)


        nCars = dict()
        for car in cars:
            if nCars.get(car["name"]):
                nCars[car["name"]].append(car)
            else:
                nCars[car["name"]] = [car,]
        return jsonify(nCars), 200

    @classmethod
    # rota -> /api/cars/123456
    def getCar(cls, carID, carName=None, carYear=None, brand=None, *args, **kwargs) -> Any:
        if all([carID, carName, carYear, brand]):
            car = Car.query.filter_by( id=carID, name=carName.title(), year=str(carYear), brand=brand.title() ).first()
            if isinstance(car, Car):
                return jsonify(car.to_dict()) , 200
        else:
            car = Car.query.filter_by( id=carID ).first()
            if isinstance(car, Car):
                return jsonify(car.to_dict()) , 200
        return jsonify({"message":f"car not found"}), 404
    
    @classmethod
    # rota -> /api/cars/Fiat/Toro
    def getCarByName(cls, brand, carName, *args, **kwargs) -> Any:
        cars = Car.query.filter_by( brand=brand.title(), name=carName.title() ).all()
        if len(cars) > 0:
            return jsonify([car.to_dict() for car in cars]) , 200
        return jsonify({"message":f"car not found"}), 404
            
    @classmethod
    # rota -> /api/cars/Fiat/Toro/2021
    def getCarByYear(cls, brand, carYear, carName, *args, **kwargs) -> Any:
        cars = Car.query.filter_by( name=carName.title(), year=str(carYear) ).all()
        if len(cars) > 0:
            return jsonify([car.to_dict() for car in cars]) , 200
        return jsonify({"message":f"car not found"}), 404




    @classmethod
    # rota -> /api/cars
    @loginRequired
    def setCar(cls, *args, **kwargs) -> Any:
        data = request.form.to_dict() or request.json
        if data is None:
            return jsonify({"message":"values is required"}),400

        for attrName, attrValue in data.items():
            if isinstance(attrValue, str):
                data[attrName] = attrValue.title()
                
        car = Car.query.filter_by(
            name=data["name"],
            year=data["year"],
            brand=data["brand"],
            engine=data["engine"]
            ).first()
        if isinstance(car,Car):
            return jsonify({
                "message": f"there is already a car with the following fields",
                "car":car.to_dict()
            }),400
        data["created_at"] = datetime.now(timezone.utc)
        car = Car(data)
        capp.db.session.add(car)
        capp.db.session.commit()
        
        return jsonify(car.to_dict()), 201
    



    @classmethod
    @loginRequired
    # rota -> /api/cars/12345
    def updateCar(cls, carID, *args, **kwargs) -> Any:
        # carID aqui é um dict
        car = None
        data = request.form.to_dict() or request.json
        if data is None:
            return jsonify({"message":"request payload is invalid"}), 400


        for attrName, attrValue in data.items():
            if isinstance(attrValue, str):
                data[attrName] = attrValue.title()

        car = Car.query.filter_by(id=carID["carID"]).first()
        attrMain = ["updated_at", "created_at", "id"]
        if isinstance(car,Car):
            for attrName,attrValue in data.items():
                if hasattr(car, attrName) and attrName not in attrMain:
                    setattr(car, attrName, attrValue)
            car.updated_at = datetime.now(timezone.utc)

            capp.db.session.add(car)
            capp.db.session.commit()
            return jsonify(car.to_dict()), 200
    

        else:
            newData = {"created_at": datetime.now(timezone.utc)}
            for attrName,attrValue in data.items():
                if attrName not in attrMain:
                    newData[attrName] = attrValue
            car = Car(newData)
            capp.db.session.add(car)
            capp.db.session.commit()

            return jsonify(car.to_dict()), 201
    




    @classmethod
    @loginRequired
    # rota -> /api/cars/12345
    def deleteCar(cls, carID, *args, **kwargs) -> Any:
        # carID aqui é um dict
        car = Car.query.filter_by(id=carID["carID"]).first()
        if isinstance(car, Car):
            capp.db.session.delete(car)
            capp.db.session.commit()
            return jsonify(), 204
        return jsonify({"message":"item not found"}), 404
