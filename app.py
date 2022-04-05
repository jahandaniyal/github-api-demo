from flask import Flask
from flasgger import Swagger
from api.route.main import app_api
from prometheus_flask_exporter import PrometheusMetrics


def create_app():
    app = Flask(__name__)

    # Initialize Config
    app.config['SWAGGER'] = {
        'title': 'GitHub API Demo App',
    }
    app.register_blueprint(app_api, url_prefix='/api')
    Swagger(app)
    PrometheusMetrics(app)

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)