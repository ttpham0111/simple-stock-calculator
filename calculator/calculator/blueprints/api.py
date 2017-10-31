from flask import Blueprint

from calculator.handlers import stocks


def register(app):
    bp = Blueprint('api', __name__)

    bp.add_url_rule('/calculate', view_func=stocks.calculate_stats, methods=['GET'])

    app.register_blueprint(bp, url_prefix='/api')
