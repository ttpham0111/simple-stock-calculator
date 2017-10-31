from flask import request, jsonify, abort

from calculator.models.stock import Stock


def calculate_stats():
    try:
        data = get_stock_data_from_request(request)
    except KeyError as e:
        return abort(400, e)

    stock = Stock.from_dict(data)
    return jsonify(stock.get_stats())


def get_stock_data_from_request(r):
    return {
        'symbol': r.args['symbol'],
        'allotment': int(r.args['allotment']),
        'initial_share_price': int(r.args['initial_share_price']),
        'final_share_price': int(r.args['final_share_price']),
        'sell_commission': int(r.args['sell_commission']),
        'buy_commission': int(r.args['buy_commission']),
        'capital_gain_tax_rate': float(r.args['capital_gain_tax_rate'])
    }
