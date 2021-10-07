import os

from flask import Flask



class Config(object):
    SECRET_KEY = SECRET_KEY='FGHJkççççghhv@J@oiuytYUIOjhgffGHJKLkjhgfertyuIOpḉloiuypṕopopṕopṕṕṕṕṕṕṕḉçḉḉḉḉ'
    TEMPLATE_AUTO_RELOAD = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self, app: "Flask", env:str) -> None:
        for attr in dir(self):
            if attr.isupper():
                app.config[attr] =  getattr(self, attr)

class DEVConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    ENV = "development"
    DEBUG = True

class TESTConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    TEMPLATE_AUTO_RELOAD = False
    TESTING = True

class PRODConfig(Config):
    TEMPLATE_AUTO_RELOAD = False
    SQLALCHEMY_DATABASE_URI = DATABASE='postgresql://jkncgvslbfymgq:e93ec0cc43d920665a0a247947c9156060984464367515b73b96bc5432bfbac9@ec2-52-72-125-94.compute-1.amazonaws.com:5432/d42erfvmcv4gfi'

class SetConfig:

    def __init__(self, app, env:str=None):
        cfgs = {"production":PRODConfig, "testing":TESTConfig, "development":DEVConfig}
        if cfgs.get(env):
            cfg = cfgs.get(env)
            cfg(app, env)
        else:
            cfg = cfgs.get("production")
            cfg(app, "production")
