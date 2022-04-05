# -*- coding: utf-8 -*-
"""
The main entry point for this flask application.
Registers blueprint for /api route and additionally,
configures flasgger and prometheus for metrics collection.
"""

from flask import Flask
from flasgger import Swagger
from prometheus_flask_exporter import PrometheusMetrics

from api.route.main import app_api


def create_app():
    """
    Configure flask application routes, swagger and prometheus
    :return: flask object
    """
    flask_app = Flask(__name__)

    # Initialize Config
    flask_app.config['SWAGGER'] = {
        'title': 'GitHub API Demo App',
    }
    flask_app.register_blueprint(app_api, url_prefix='/api')
    Swagger(flask_app)
    PrometheusMetrics(flask_app)

    return flask_app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
