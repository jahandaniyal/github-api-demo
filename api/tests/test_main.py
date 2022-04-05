class TestApp:
    def test_popularity_public_repo(self, client,):
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
        url = '/api/stats/jahandaniyal/Algorithms-CC'
        response = client.get(url, headers=None)
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404

    def test_invalid_owner_fails(self, client):
        url = '/api/stats/invaliduser/hello-world'
        response = client.get(url, headers=None)
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404

    def test_invalid_repo_fails(self, client):
        url = '/api/stats/octocat/invalidrepo'
        response = client.get(url, headers=None)
        assert response.get_json()['error']['message'] == 'Not Found'
        assert response.status_code == 404



