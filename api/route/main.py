from http import HTTPStatus
from flask import Blueprint, jsonify

app_api = Blueprint('api', __name__)


@app_api.route('/')
def ping_server():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    return jsonify({"status": "OK"}), HTTPStatus.OK
