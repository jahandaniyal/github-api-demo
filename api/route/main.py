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
    """
    # Stats endpoint API Specification
    # Return a string message

    ---
    parameters:
      - name: owner
        in: path
        type: string
        required: true
        description: Must be an active GitHub Account
      - name: repo
        in: path
        type: string
        required: true
        description: Must be a valid Git repository
      - name: X-Github-Token
        in: header
        schema:
            type: string
        required: false
        description: GitHub API Token
    definitions:
          Popularity:
            type: string
    responses:
      200:
        description: Returns True if a repository is popular else False.
        examples:
            application/json: |
              {
                popular: True
              }
      404:
        description:
        examples:
            application/json: |
                {
                    "error": {
                        "documentation_url": "https://docs.github.com/rest/reference/repos#get-a-repository",
                        "message": "Not Found"
                    }
                }
    :param owner (str): GitHub Account name
    :param repo (str): Git Repository name
    :return (bool): True is repository is popular else False
    """
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
