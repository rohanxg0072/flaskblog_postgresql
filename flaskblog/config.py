import json

with open("config.json") as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    MAIL_SERVER = config.get("MAIL_SERVER")
    MAIL_PORT = config.get("MAIL_PORT")
    MAIL_USE_TLS = config.get("MAIL_USE_TLS")
    MAIL_USERNAME = config.get("MAIL_USER")
    MAIL_PASSWORD = config.get("MAIL_PASS")

