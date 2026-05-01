import argparse
import logging
from bot.client import BinanceClient
from bot.orders import create_order
from bot.validators import validate_input
from bot.logging_config import setup_logger

setup_logger()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        client = BinanceClient("YOUR_API_KEY", "YOUR_SECRET")

        response = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Placed Successfully")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        logging.info(f"Order success: {response}")

    except Exception as e:
        print("\n❌ Order Failed:", str(e))
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()