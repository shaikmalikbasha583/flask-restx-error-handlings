import logging
import os

import coloredlogs
from flask import Flask, jsonify, make_response, send_from_directory
from flask_restx._http import HTTPStatus
from werkzeug.exceptions import BadRequest

from app.main.extensions.flask_extensions import api
from app.main.resources.info_resource import InfoResource, info_namespace
from app.main.resources.error_resource import error_namespace
from app.main.utils import constants

# Make sure to define the logger object
logger = logging.getLogger(__name__)
coloredlogs.install(
    level="INFO", fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


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
    logging.info("Index API processing...")
    r = {"msg": "Welcome to FlaskRestX Application", "docs_url": constants.API_DOCS_URL}
    logging.info(f"Index API Response: {r}")
    return r


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
