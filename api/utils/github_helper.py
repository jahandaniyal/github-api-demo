import requests
import os, json
from pprint import pprint

from api.schema.popularity import PopularitySchema
from api.utils.custom_exceptions import ResourceNotAvailable

_TOKEN = os.getenv('GITHUB_TOKEN')
_GITHUB_REPOS_BASE_URL = "https://api.github.com/repos/"



class GitHubAPI:
    def __init__(self, owner, repo, token=_TOKEN):
        self.owner = owner
        self.repo = repo
        self.forks_count = 0
        self.stars_count = 0
        self.url = "{}{}/{}".format(_GITHUB_REPOS_BASE_URL, owner, repo)
        self.headers = {'Authorization': 'token {}'.format(token)} if token else None

    def get_repo(self):
        req = requests.get(self.url, headers=self.headers)
        if req.status_code != 200:
            raise ResourceNotAvailable(req.json(), req.status_code)
        data = PopularitySchema().load(req.json(), unknown='exclude')
        self.forks_count = data.get('forks')
        self.stars_count = data.get('stars')
        # pprint(req.json())
        return req

    def is_popular(self):
        if self.forks_count * 2 + self.stars_count >= 500:
            return True, "{}'s repository '{}' is popular ".format(self.owner, self.repo)
        return False, "{}'s repository '{}' is NOT popular".format(self.owner, self.repo)
