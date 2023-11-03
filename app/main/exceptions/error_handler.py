from flask import jsonify, make_response
from flask_restx._http import HTTPStatus

# from app.main import app
from werkzeug.exceptions import BadRequest, NotFound

from app.main.extensions.flask_extensions import api

# @app.errorhandler(BadRequest)
# def handle_404_error(e):
#     print(e)
#     return make_response(jsonify({"msg": "Page not found!"}), 404)


# @app.errorhandler(NotFound)
# def handle_not_found(e):
#     print(e)
#     return {"msg": "Page Not Found"}, 404


# @api.errorhandler(HTTPStatus.NOT_FOUND)
# def handle_404_error(e):
#     print(e)
#     return make_response(jsonify({"msg": "Page not found!"}), HTTPStatus.NOT_FOUND)


# @api.errorhandler(Exception)
# def handle_custom_exception(error):
#     """Return a custom message and 400 status code"""
#     print("Exactly I am expecting this")
#     print(error)
#     return {"message": "What you want"}, 400


class CustomException(Exception):
    # def __init__(self, message) -> None:
    #     self.message = message

    def __init__(self, error_code, success, message, desc, status_code):
        self.error_code = error_code
        self.success = success
        self.message = message
        self.desc = desc
        self.status_code = status_code

    # @property
    # def get_message(self):
    #     return {
    #         "error_code": self.error_code,
    #         "success": self.success,
    #         "msg": self.msg,
    #         "desc": self.desc,
    #         "status_code": self.status_code,
    #     }

    def to_dict(self) -> str:
        return {
            "error_code": self.error_code,
            "success": self.success,
            "msg": self.msg,
            "desc": self.desc,
            "status_code": self.status_code,
        }
