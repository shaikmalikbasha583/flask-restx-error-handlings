import json
from http import HTTPStatus
from typing import Any, Iterable, Mapping

from flask import jsonify
from werkzeug.wrappers import Response


def success_response(
    app_cde: str, success: bool = True, message: str = "", data: Any = {}
):
    return jsonify(
        {"app_code": app_cde, "success": success, "message": message, "data": data}
    )


class SuccessResponse:
    def __init__(self, success: bool = True, message: str = "", data: Any = {}) -> None:
        self.success = success
        self.message = message
        self.data = data

    def __repr__(self) -> str:
        return json.dumps(*self)

    def to_dict(self) -> dict:
        return {"success": self.success, "message": self.message, "data": self.data}

    # def __init__(
    #     self,
    #     response=None,
    #     status=None,
    #     headers=None,
    #     mimetype=None,
    #     content_type=None,
    #     direct_passthrough=False,
    # ) -> None:
    #     super().__init__(
    #         response, status, headers, mimetype, content_type, direct_passthrough
    #     )
