import requests
import json

# Fetch current market data from CoinGecko API
def get_live_price(crypto_symbol: str):
    """
    Fetches the live price for a given cryptocurrency symbol from the CoinGecko API.
    
    :param crypto_symbol: The symbol of the cryptocurrency (e.g., 'bitcoin', 'ethereum').
    :return: The current price of the cryptocurrency in USD.
    """
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto_symbol]['usd']
    else:
        raise Exception("Failed to fetch data from CoinGecko API")
