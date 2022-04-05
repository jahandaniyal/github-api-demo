from flask import Blueprint, jsonify, request
from http import HTTPStatus

from api.utils.github_helper import GitHubAPI, ResourceNotAvailable

app_api = Blueprint('api', __name__)


@app_api.route('/')
def ping_server():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    return jsonify({"status": "OK"}), HTTPStatus.OK


@app_api.route('/stats/<owner>/<repo>', methods=['GET'])
def github_repo_stats(owner, repo):
    gitstats = GitHubAPI(owner, repo, request.headers.get('X-Github-Token'))
    try:
        gitstats.get_repo()
        result, message = gitstats.is_popular()
    except ResourceNotAvailable as rna:
        return jsonify({"error": rna.message}), rna.status_code
    except Exception as ex:
        return jsonify({"error": ex.message}), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return jsonify(message), HTTPStatus.OK
