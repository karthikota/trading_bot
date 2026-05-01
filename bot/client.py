import random
import time

class BinanceClient:
    def __init__(self, api_key=None, api_secret=None, mock=True):
        self.mock = mock

    def place_order(self, params):
        if self.mock:
            return self._mock_response(params)
        else:
            raise NotImplementedError("Real API not configured")

    def _mock_response(self, params):
        return {
            "symbol": params["symbol"],
            "side": params["side"],
            "type": params["type"],
            "orderId": random.randint(100000, 999999),
            "status": "FILLED",
            "executedQty": params["quantity"],
            "avgPrice": params.get("price", str(round(random.uniform(60000, 70000), 2))),
            "timestamp": int(time.time() * 1000)
        }