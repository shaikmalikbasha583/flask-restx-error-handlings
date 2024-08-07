import logging

from app.main.responses.api_response import SuccessResponse, success_response
from app.main.utils import constants


def get_info_details():
    logging.info("COLOREDLOGS: I am fetching info details...")
    logging.debug("COLOREDLOGS: I am fetching debug details...")
    logging.warning("COLOREDLOGS: I am fetching warning details...")
    logging.error("COLOREDLOGS: I am fetching error details...")
    logging.critical("COLOREDLOGS: I am fetching critical details...")
    data = {
        "success": True,
        "app_name": constants.APP_NAME,
        "app_module": constants.APP_MODULE,
        "app_code": constants.APP_CODE,
        "build": {"version": constants.APP_VERSION},
    }
    # return success_response(
    #     "APP_01", True, "Successfully fetches the INFO data", data=data
    # )
    r = SuccessResponse(True, "I am SuccesClassMesg", data).serialize()
    logging.info(r)
    return r
