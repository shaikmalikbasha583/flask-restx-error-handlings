import logging

from app.main.responses.api_response import SuccessResponse, success_response
from app.main.utils import constants


def get_info_details():
    logging.info("I am fetching info details...")
    data = {
        "success": True,
        "app_name": constants.APP_NAME,
        "app_module": constants.APP_MODULE,
        "app_code": constants.APP_CODE,
        "build": {"version": constants.APP_VERSION},
    }
    # success_response("APP_01", True, "Successfully fetches the INFO data", data=data)
    r = SuccessResponse(True, "I am SuccesClassMesg", data).to_dict()
    logging.info(r)
    return r
