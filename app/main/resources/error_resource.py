import logging
from email import message

from flask_restx import Namespace
from flask_restx._http import HTTPStatus
from werkzeug.exceptions import BadRequest, InternalServerError

from app.main.exceptions.error_handler import CustomException
from app.main.extensions.flask_extensions import api

error_namespace = Namespace(name="Errors", description="Errors/Exceptions", path="/")


@error_namespace.errorhandler(CustomException)
def custom_error_handler(e):
    # print(e.to_dict())
    # print(getattr(e, "code", 500))
    # res = make_response(jsonify({e.to_dict()}), HTTPStatus.BAD_REQUEST)
    return {
        "Okay": "Bhai",
        "message": e.message,
        "app_code": e.error_code,
        "desc": e.desc,
    }, HTTPStatus.BAD_REQUEST
    # return e.to_dict(), 400


@error_namespace.errorhandler(BadRequest)
def index_error(e):
    logging.info("Why am I executing...")
    logging.info(e)
    return {"Okay": "Bad Request"}, HTTPStatus.BAD_REQUEST


@error_namespace.errorhandler(Exception)
def internal_server_error(e):
    desc = getattr(e, "message", repr(e))
    return {
        "success": False,
        "message": "Internal Server Error",
        "description": str(desc),
    }, HTTPStatus.INTERNAL_SERVER_ERROR
