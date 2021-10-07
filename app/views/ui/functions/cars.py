import json

from typing import Any

from flask import render_template

from app.model.tables.cars import Car
from app.model.tables.brands import Brand


class CarUI:

    @classmethod
    def getCars(cls, brand, *args, **kwargs) -> Any:
        b = Brand.query.filter_by(name=brand.title()).first()
        if isinstance(b,Brand):
            return render_template("/main/cars.html" , *args, **kwargs, brand=b.name), 200
        return render_template("main/notFound.html"), 400

    @classmethod
    def getCar(cls, brand, carName, carYear, carID, *args, **kwargs) -> Any:
        car = Car.query.filter_by(id=carID).first()
        if isinstance(car, Car):
            return render_template("/main/car.html" , *args, **kwargs, car=json.dumps(car.to_dict())), 200
        return render_template("/main/notFound.html" , *args, **kwargs), 404
