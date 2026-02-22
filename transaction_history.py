import json
from src.encryption import encrypt_data, decrypt_data

class TransactionHistory:
    def __init__(self, key):
        self.key = key
        self.history = []

    def add_transaction(self, crypto_symbol, amount, price, date):
        """
        Add a transaction to the history.
        
        :param crypto_symbol: The cryptocurrency symbol (e.g., 'bitcoin').
        :param amount: Amount of cryptocurrency bought/sold.
        :param price: Price at which the transaction occurred.
        :param date: Date of the transaction.
        """
        transaction = {
            'symbol': crypto_symbol,
            'amount': amount,
            'price': price,
            'date': date
        }
        encrypted_transaction = encrypt_data(json.dumps(transaction), self.key)
        self.history.append(encrypted_transaction)

    def get_history(self):
        """
        Returns the transaction history (decrypted).
        
        :return: Decrypted transaction history.
        """
        return [json.loads(decrypt_data(item, self.key)) for item in self.history]
