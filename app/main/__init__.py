import logging
import os

import coloredlogs
import httpx
from flask import Flask, jsonify, make_response, send_from_directory
from flask_restx._http import HTTPStatus
from werkzeug.exceptions import BadRequest

from app.main.extensions.flask_extensions import api
from app.main.resources.error_resource import error_namespace
from app.main.resources.info_resource import InfoResource, info_namespace
from app.main.utils import constants

print(f"APP ENVIRONMENT: {os.environ.get('ENV')}")

# Make sure to define the logger object
logger = logging.getLogger(__name__)

log_level = "INFO"
fmt_str = r"[%(asctime)s] - %(name)s - P%(process)s - %(levelname)s: %(message)s"
if os.environ.get("ENV") in [None, "development"]:
    log_level = "DEBUG"
# fmt_str = r"[%(asctime)s] p%(process)s %(filename)s:%(lineno)d %(levelname)s - %(message)s"
# fmt_str = "%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in function %(funcName)s] %(message)s"

coloredlogs.install(level=log_level, fmt=fmt_str)


## Create the Flask App Object and add basic configuration to it
app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    icon_dir = os.path.join(os.getcwd(), "app", "main", "static", "icons")
    return send_from_directory(
        icon_dir, "shortcut-icon", mimetype="image/vnd.microsoft.icon"
    )


@app.route("/")
def index():
    logging.info("INFO: Index API processing...")
    logging.debug("DEBUG: Index API processing...")
    r = {"msg": "Welcome to FlaskRestX Application", "docs_url": constants.API_DOCS_URL}
    logging.info(f"Index API Response: {r}")
    return r


@app.route("/data")
def get_data():
    URL = "https://jsonplaceholder.typicode.com/todos/1"
    req = httpx.request("GET", URL)
    return req.json()


@api.errorhandler(BadRequest)
def handle_404_error(e):
    print(e)
    return make_response(jsonify({"msg_1": "Page not found!"}), 404)


## Add namespaces to the api object
api.add_namespace(info_namespace)
api.add_namespace(error_namespace)

## Routers
## Actuator Routers
info_namespace.add_resource(InfoResource, "/info")
