from flask import g
from flask import request
from flask import session

from flask import jsonify
from flask import redirect
from flask import url_for

from app.model.tables.users import User


def nonLogin(func):
    doc = func.__doc__
    name = func.__name__
    def decorator( *args, **kw):
        u = session.get("user")
        if u is not None:
            u = User.query.filter_by(email=u).first()
            if isinstance(u, User):
                if request.blueprint == "api":
                    return jsonify({"message":"You are already logged in"})
                return redirect("/")
        return func(args, kw)
    decorator.__name__ = name
    decorator.__doc__ = doc
    return decorator


def loginRequired(func):
    doc = func.__doc__
    name = func.__name__
    def decorator( *args, **kw):
        u = session.get("user")
        n = request.url
        if u is not None:
            u = User.query.filter_by(email=u).first()
            if isinstance(u, User):
                g.user = u
                return func(args, kw)
        if request.blueprint == "api":
            return jsonify({
                "message":"You must be logged in to access this feature.",
                "url":url_for("auth.loginGetApi")
            }),401
        return redirect(url_for("auth.loginGet", next=n))
    decorator.__name__ = name
    decorator.__doc__ = doc
    return decorator

def getUser():
    if "user" not in g:
        g.user = False
        u = session.get("user")
        if u is not None:
            u = User.query.filter_by(email=u).first()
            if isinstance( u, User ):
                g.user = u