# -*- coding: utf-8 -*-
"""
Tests for popularity check functionality
"""


class TestPopularityApp:
    """
    All the tests for Popularity check functionality
    """
    def test_popularity_public_repo(self, client,):
        """
        Test if a public repository is popular or not.
        Additionally, checks that no GitHub API token is required for
        public repositories.
        :param client:
        :return:
        """
        # Test a popular repository
        url = '/api/stats/octocat/hello-world'
        response = client.get(url, headers=None)
        assert response.get_json() == {'popular': True}
        assert response.status_code == 200

        # Test a repository which is not popular
        url = '/api/stats/octocat/git-consortium'
        response = client.get(url, headers=None)
        assert response.get_json() == {'popular': False}
        assert response.status_code == 200

    def test_private_repo(self, client):
        """
        Test that popularity of private repository is not available
        for missing or invalid GitHub Token header.
        :param client:
        :return:
        """
        # Test missing GitHub token fails
        url = '/api/stats/jahandaniyal/Algorithms-CC'
        response = client.get(url, headers=None)
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404

        # Test invalid GitHub token fails
        url = '/api/stats/jahandaniyal/Algorithms-CC'
        response = client.get(url, headers='invalid_token_example')
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404

    def test_invalid_owner_fails(self, client):
        """
        Tests that request fails for invalid GitHub User.
        :param client:
        :return:
        """
        url = '/api/stats/invaliduser/hello-world'
        response = client.get(url, headers=None)
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404

    def test_invalid_repo_fails(self, client):
        """
        Tests that request fails for invalid Git Repository.
        :param client:
        :return:
        """
        url = '/api/stats/octocat/invalidrepo'
        response = client.get(url, headers=None)
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404
