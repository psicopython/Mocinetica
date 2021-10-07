from flask import Flask
from flask import Blueprint

from . import auth
from . import api
from . import ui

from .auth.functions.utils import getUser


class Views:

    _listOfRouters = [auth.router, api.router, ui.router]

    def __init__(self, app:"Flask"):
        for r in self._listOfRouters:

            bp = Blueprint(name=r["config"]["name"], import_name="app")
            for attrName, attrValue in r["config"].items():
                if hasattr(bp, attrName):
                    setattr(bp, attrName, attrValue)

            for route in r["routes"]:
                bp.add_url_rule(
                    rule = route["rule"],
                    methods = route["methods"],
                    endpoint = route["endpoint"],
                    view_func = route["view_func"],
                )
            app.register_blueprint(bp)
        app.before_request(getUser)

