from http import HTTPStatus
from flask import Blueprint, request



bp = Blueprint('index', __name__, url_prefix='/common')


@bp.route('debug')
# @Http.make_cross_resp
def debug():
    1 / 0
    return ''


@bp.route('health_check')
# @Http.make_cross_resp
def health_check():
    return {
        "code": HTTPStatus.OK,
        "msg": "success"
    }


@bp.route('reset')
# @Http.make_cross_resp
def reset_mock_data():
    return {
        "code": HTTPStatus.OK,
        "msg": "success"
    }
