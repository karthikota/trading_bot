import random
import time
import logging

class BinanceClient:
    def __init__(self, api_key=None, api_secret=None, mock=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.mock = mock

    def place_order(self, params: dict) -> dict:
        """
        Places an order (mock or real).
        """
        try:
            logging.info(f"Placing order: {params}")

            if self.mock:
                response = self._mock_response(params)
            else:
                raise NotImplementedError("Real API not configured")

            logging.info(f"Order success: {response}")
            return response

        except Exception as e:
            logging.error(f"Order failed: {str(e)}")
            raise

    def _mock_response(self, params: dict) -> dict:
        """
        Simulates Binance Futures order response.
        """
        price = params.get("price")

        # If MARKET, simulate price
        if params["type"] == "MARKET":
            price = str(round(random.uniform(60000, 70000), 2))

        return {
            "symbol": params["symbol"],
            "side": params["side"],
            "type": params["type"],
            "orderId": random.randint(100000, 999999),
            "status": "FILLED",
            "executedQty": str(params["quantity"]),
            "avgPrice": price,
            "timestamp": int(time.time() * 1000)
        }