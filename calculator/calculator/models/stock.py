from collections import namedtuple


_Stock = namedtuple('Stock', [
    'symbol',
    'allotment',
    'initial_share_price',
    'final_share_price',
    'sell_commission',
    'buy_commission',
    'capital_gain_tax_rate'
])


class Stock(_Stock):
    __slots__ = ()

    @classmethod
    def from_dict(cls, d):
        return cls(symbol=d['symbol'],
                   allotment=d['allotment'],
                   initial_share_price=d['initial_share_price'],
                   final_share_price=d['final_share_price'],
                   sell_commission=d['sell_commission'],
                   buy_commission=d['buy_commission'],
                   capital_gain_tax_rate=d['capital_gain_tax_rate'] / 100.0)

    @property
    def proceeds(self):
        return self.allotment * self.final_share_price

    @property
    def cost(self):
        return self.purchase_price + self.total_commission + self.tax

    @property
    def total_commission(self):
        return self.buy_commission + self.sell_commission

    @property
    def purchase_price(self):
        return self.allotment * self.initial_share_price

    @property
    def pre_tax_profit(self):
        return self.proceeds - (self.purchase_price + self.total_commission)

    @property
    def tax(self):
        return self.capital_gain_tax_rate * self.pre_tax_profit

    @property
    def net_profit(self):
        return self.proceeds - self.cost

    @property
    def return_on_investment(self):
        return self.net_profit / self.cost

    @property
    def break_even_price(self):
        return (self.purchase_price + self.total_commission) / float(self.allotment)

    def get_stats(self):
        return {
            'proceeds': self.proceeds,
            'cost': self.cost,
            'net_profit': self.net_profit,
            'return_on_investment': self.return_on_investment,
            'break_even_price': self.break_even_price
        }

    def print_stats(self):
        stats = '\n'.join([
            'PROFIT REPORT:',
            'Proceeds', '${:,}'.format(self.proceeds), '',
            'Cost', '${:,}'.format(self.cost), '',
            'Cost details:',
            'Total Purchase Price',
            '{} x ${} = {:,.2f}'.format(self.allotment, self.initial_share_price, self.purchase_price),
            'Buy Commission = {:.2f}'.format(self.buy_commission),
            'Sell Commission = {:.2f}'.format(self.sell_commission),
            'Tax on Capital Gain = {}% of ${:,.2f} = {:,}'.format(int(self.capital_gain_tax_rate * 100),
                                                                  self.pre_tax_profit, self.tax), '',
            'Net Profit', str(self.net_profit), '',
            'Return on Investment', '{:.2f}%'.format(self.return_on_investment * 100), '',
            'To break even, you should have a final share price of', '${:.2f}'.format(self.break_even_price)
        ])
        print(stats)
