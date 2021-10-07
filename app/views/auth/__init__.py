from .functions import Login

router = {
    "config": {
        "name": "auth",
        "url_prefix": "/auth"
    },
    "routes": [
        {
            "rule": "/login",
            "methods": ["POST"],
            "endpoint": "loginPost",
            "view_func": Login.loginPost
        },
        {
            "rule": "/logout",
            "methods": ["GET","POST"],
            "endpoint": "logout",
            "view_func": Login.logout
        }
    ]
}