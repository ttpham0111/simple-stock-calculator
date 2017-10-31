from calculator.models.stock import Stock


def get_stock_data_from_cli():
    return {
        'symbol': raw_input('Symbol: '),
        'allotment': int(raw_input('Allotment: ')),
        'initial_share_price': int(raw_input('Initial Share Price: ')),
        'final_share_price': int(raw_input('Final Share Price: ')),
        'sell_commission': int(raw_input('Sell Commission: ')),
        'buy_commission': int(raw_input('Buy Commission: ')),
        'capital_gain_tax_rate': float(raw_input('Capital Gain Tax Rate: '))
    }


def main():
    data = get_stock_data_from_cli()
    stock = Stock.from_dict(data)
    stock.print_stats()


if __name__ == '__main__':
    main()
