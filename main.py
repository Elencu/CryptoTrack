import argparse
from src.portfolio import Portfolio
from src.transaction_history import TransactionHistory
from src.encryption import generate_key

def main():
    parser = argparse.ArgumentParser(description="CryptoTrack CLI")
    parser.add_argument('--add-asset', help="Add cryptocurrency to portfolio (symbol,amount)", type=str)
    parser.add_argument('--view-portfolio', help="View portfolio value", action='store_true')
    args = parser.parse_args()

    # Generate a new encryption key for secure storage
    key = generate_key()

    portfolio = Portfolio()
    transaction_history = TransactionHistory(key)

    if args.add_asset:
        symbol, amount = args.add_asset.split(',')
        portfolio.add_asset(symbol, float(amount))
        print(f"Added {amount} {symbol} to portfolio.")

        # Example transaction log
        transaction_history.add_transaction(symbol, float(amount), 50000, '2026-02-20')

    if args.view_portfolio:
        total_value = portfolio.get_total_value()
        print(f"Total portfolio value: ${total_value:.2f}")

    print("Transaction History:")
    history = transaction_history.get_history()
    for transaction in history:
        print(transaction)

if __name__ == "__main__":
    main()
