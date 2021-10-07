
from .functions.car import CarResources
from .functions.brand import BrandResources

router = {
    "config": {
        "name": "api",
        "url_prefix": "/api"
    },
    "routes": [
        # CAR Routes
        {
            "rule":"/cars",
            "methods": ["POST"],
            "endpoint": "setCar",
            "view_func": CarResources.setCar
        },{
            "rule":"/cars/<string:brand>",
            "methods": ["GET"],
            "endpoint": "getCars",
            "view_func": CarResources.getCars
        },{
            "rule":"/cars/<string:brand>/<string:carName>",
            "methods": ["GET"],
            "endpoint": "getCarByName",
            "view_func": CarResources.getCarByName
        },{
            "rule":"/cars/<string:brand>/<string:carName>/<int:carYear>",
            "methods": ["GET"],
            "endpoint": "getCarByYear",
            "view_func": CarResources.getCarByYear
        },{
            "rule":"/cars/<string:brand>/<string:carName>/<int:carYear>/<int:carID>",
            "methods": ["GET"],
            "endpoint": "getCarByIDFull",
            "view_func": CarResources.getCar
        },{
            "rule":"/cars/<int:carID>",
            "methods": ["GET"],
            "endpoint": "getCarByID",
            "view_func": CarResources.getCar
        },{
            "rule":"/cars/<int:carID>",
            "methods": ["PUT"],
            "endpoint": "updateCar",
            "view_func": CarResources.updateCar
        },{
            "rule":"/cars/<int:carID>",
            "methods": ["DELETE"],
            "endpoint": "deleteCar",
            "view_func": CarResources.deleteCar
        },
        
        # BRAND Routes
        {
            "rule":"/brands",
            "methods": ["GET"],
            "endpoint": "getBrands",
            "view_func": BrandResources.getBrands
        },{
            "rule":"/brands",
            "methods": ["POST"],
            "endpoint": "setBrand",
            "view_func": BrandResources.setBrand
        },{
            "rule":"/brands/<int:brandID>",
            "methods": ["GET"],
            "endpoint": "getBrand",
            "view_func": BrandResources.getBrand
        },{
            "rule":"/brands/<int:brandID>",
            "methods": ["PUT"],
            "endpoint": "updateBrand",
            "view_func": BrandResources.updateBrand
        },{
            "rule":"/brands/<int:brandID>",
            "methods": ["DELETE"],
            "endpoint": "deleteBrand",
            "view_func": BrandResources.deleteBrand
        }
    ]
}