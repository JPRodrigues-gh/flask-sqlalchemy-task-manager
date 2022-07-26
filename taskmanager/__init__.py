"""
initialize our taskmanager application as a package, allowing
us to use our own imports, as well as any standard imports
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECURITY_KEY"] = os.environ.get("SECURITY_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)

from taskmanager import routes  # noqa
