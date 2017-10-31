from flask import Flask

from calculator import blueprints


def get_app():
    app = Flask(__name__, static_folder='public')

    blueprints.api.register(app)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app


def main():
    app = get_app()
    app.run()


if __name__ == '__main__':
    main()
