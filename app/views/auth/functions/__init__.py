from flask import redirect
from flask import jsonify
from flask import request
from flask import session

from app.model.tables.users import User

from .utils import nonLogin

    
class Login(object):
    
    @classmethod
    @nonLogin
    def loginPost(cls, *args, **kwargs):
        data = request.form.to_dict() or request.json
        n = request.args.get("next") or "/"
        if data is not None:
            if data.get("user") and data.get("password"):
                u = User.query.filter_by(email=data["user"]).first()
                if isinstance(u, User):
                    if u.checkPassword(data["password"]):
                        session["user"] = u.email
                        return jsonify({
                            "message":"successfully logged in",
                            "location": n
                            }), 200

                return jsonify({"message":"user or password is invalid"}), 401
        return jsonify({"message":"user and password is required"}), 400
    
    @classmethod
    def logout(cls, *args, **kwargs):
        if session.get("user"):
            session.pop("user")
        return redirect("/")
    
