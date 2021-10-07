from .functions.cars import CarUI
from .functions.brands import BrandUI

router = {
    "config": {
        "name": "ui"
    },
    "routes": [

        {
            "rule": "/",
            "methods": ["GET"],
            "endpoint": "listBrands",
            "view_func": BrandUI.listBrands,
        },
        {
            "rule": "/<string:brand>/",
            "methods": ["GET"],
            "endpoint": "getCars",
            "view_func": BrandUI.listBrands,
        },
        {
            "rule": "/<string:brand>/<string:carName>/",
            "methods": ["GET"],
            "endpoint": "getCarByName",
            "view_func": BrandUI.listBrands,
        },
        {
            "rule": "/<string:brand>/<string:carName>/<int:carYear>/",
            "methods": ["GET"],
            "endpoint": "getCarByYear",
            "view_func": BrandUI.listBrands,
        },
        {
            "rule": "/<string:brand>/<string:carName>/<int:carYear>/<int:carID>/",
            "methods": ["GET"],
            "endpoint": "getCarByIDFull",
            "view_func": BrandUI.listBrands,
        },
        {
            "rule": "/<string:brand>/<int:carID>/",
            "methods": ["GET"],
            "endpoint": "getCarByID",
            "view_func": BrandUI.listBrands,
        },
    ]
}