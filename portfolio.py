from src.crypto_data import get_live_price

class Portfolio:
    def __init__(self):
        self.assets = {}

    def add_asset(self, crypto_symbol, amount):
        """
        Add an asset to the portfolio.
        
        :param crypto_symbol: The symbol of the cryptocurrency (e.g., 'bitcoin').
        :param amount: Amount of the cryptocurrency held.
        """
        self.assets[crypto_symbol] = amount

    def get_total_value(self):
        """
        Calculates the total value of the portfolio based on live prices.
        
        :return: Total portfolio value in USD.
        """
        total_value = 0
        for symbol, amount in self.assets.items():
            price = get_live_price(symbol)
            total_value += price * amount
        return total_value
