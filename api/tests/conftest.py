# -*- coding: utf-8 -*-
"""
Configuration settings required by pytest.
"""

import pytest
from app import create_app


@pytest.fixture()
def app():
    """
    Initialise a test flask app and configure it for TESTING purpose.
    :return: NoneType
    """
    test_app = create_app()
    test_app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield test_app
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    """
    Create test API client for all tests.
    :param app: Flask application
    :return: test_client_class
    """
    return app.test_client()


@pytest.fixture()
def runner(app):
    """
    Create a CLI runner for testing CLI commands
    :param app: Flask application
    :return: test_cli_runner_class
    """
    return app.test_cli_runner()
