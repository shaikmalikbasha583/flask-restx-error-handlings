import logging

from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource, abort, fields, reqparse
from flask_restx._http import HTTPStatus
from werkzeug.exceptions import BadRequest

from app.main.exceptions.error_handler import CustomException
from app.main.extensions.flask_extensions import api
from app.main.services.info_service import get_info_details

info_namespace = Namespace(
    name="Actuator", description="Actuator APIs/Resources", path="/"
)

## This request Parser is used for Query Params
parser = reqparse.RequestParser()
parser.add_argument("active", type=str, required=True, choices=("yes", "no"))


info_api = api.model(
    "InfoAPI",
    {"name": fields.String(required=True)},
)


class InfoResource(Resource):
    @info_namespace.doc()
    def get(self):
        print(" I am inside Resource...")
        det = get_info_details()
        logging.info(det)
        # raise CustomException(
        #     "APP_01", False, "Random Msg", "Random Desc", HTTPStatus.BAD_REQUEST
        # )
        # raise CustomException("User was not found")
        # abort(HTTPStatus.BAD_REQUEST, message="Its a bad request", custom="I am value")
        # raise BadRequest(description="I am Bad descriptin", custom="I am custom")
        # raise HTTPException(description="Not Found")
        return det, HTTPStatus.OK

    @info_namespace.doc()
    @info_namespace.expect(info_api, parser)
    def post(self):
        logging.info(parser.parse_args())
        logging.info(request.get_json())
        # raise CustomException("I am Custom Exception")
        raise CustomException(
            "APP_01", False, "Random Msg", {"desc": "desc-1"}, HTTPStatus.BAD_REQUEST
        )
        return {
            "msg": "Accepted",
            "status_code": HTTPStatus.ACCEPTED,
        }, HTTPStatus.ACCEPTED


# @info_namespace.errorhandler(CustomException)
# def custom_error_handler(e):
#     # print(e.to_dict())
#     # print(getattr(e, "code", 500))
#     # res = make_response(jsonify({e.to_dict()}), HTTPStatus.BAD_REQUEST)
#     return {"Okay": "Bhai"}, HTTPStatus.BAD_REQUEST
#     # return e.to_dict(), 400


# @info_namespace.errorhandler(BadRequest)
# def index_error(e):
#     print("Why am I executing...")
#     print(e)
#     return {"Okay": "Bad Request"}, HTTPStatus.BAD_REQUEST


# @info_namespace.errorhandler(BadRequest)
# def handle_badrequest(e):
#     print(e)
#     return {"Bad": "Request"}, HTTPStatus.BAD_REQUEST
