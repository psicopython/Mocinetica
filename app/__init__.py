from flask import Flask

from app.config import SetConfig
from app.model import Model
from app.views import Views


def create_app(env: str = "production", *args, **kwargs):
    app = Flask(
        "app",
        template_folder="front/html",
        static_folder="front/assets",
        static_url_path="/assets"
    )
    SetConfig(app, env)
    Model(app)
    Views(app)

    return app