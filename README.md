# Binance Futures Trading Bot (Testnet / Mock)

## Setup
pip install -r requirements.txt

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Features
- Supports BUY / SELL
- MARKET and LIMIT orders
- CLI input validation
- Logging system
- Error handling

## Note
Designed with modular architecture for easy extension to advanced strategies.
Due to Binance Testnet API access issues, a mock mode is implemented.
The structure supports real API integration easily.
