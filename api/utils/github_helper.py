# -*- coding: utf-8 -*-
"""
This module contains all the custom exception classes
used in this flask application.
"""

import os
import requests

from api.schema.popularity import PopularitySchema
from api.utils.custom_exceptions import ResourceNotAvailable

_TOKEN = os.getenv('GITHUB_TOKEN')
_GITHUB_REPOS_BASE_URL = "https://api.github.com/repos/"


class GitHubAPI:
    """
    This class implements methods get_repo and is_popular to get popularity
    statistics for a particular git repository.
    """
    def __init__(self, owner, repo, token=_TOKEN):
        self.owner = owner
        self.repo = repo
        self.forks_count = 0
        self.stars_count = 0
        self.url = f"{_GITHUB_REPOS_BASE_URL}{owner}/{repo}"
        self.headers = {'Authorization': f'token {token}'} if token else None

    def get_repo(self):
        """
        Use GitHub API to retreive repository information
        and additionally set forks_count and stars_count.
        :return: requests object
        """
        req = requests.get(self.url, headers=self.headers)
        if req.status_code != 200:
            raise ResourceNotAvailable(req.json(), req.status_code)
        data = PopularitySchema().load(req.json(), unknown='exclude')
        self.forks_count = data.get('forks')
        self.stars_count = data.get('stars')
        return req

    def is_popular(self):
        """
        Checks if repository is popular or not.
        :return: (Bool, String)
        """
        if self.forks_count * 2 + self.stars_count >= 500:
            return True, {"popular": True}
        return False, {"popular": False}
