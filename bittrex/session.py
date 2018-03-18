from .base import BittrexBaseSession
import requests
from .exceptions import ResponseError, RequestError


class BittrexSession(BittrexBaseSession):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = requests.session()

    def _get(self, url, payload=None):
        """HTTP GET request"""

        headers = {'apisign': self._sign_url(url)}
        response = self.session.get(url, json=payload, headers=headers)

        if response.status_code != requests.codes.ok:
            raise ResponseError(
                f'{response.url} {response.status_code}: {response.content}'
            )

        json_response = response.json()

        return self._parse_response(json_response)

    def get_markets(self, market_name=None):
        """Added our own get single market option"""
        url = self._get_markets()

        markets = self._get(url)

        if market_name is not None:
            for market in markets:
                if market_name == market.market_name:
                    break
            else:
                raise RequestError(f'Could not find {market_name}')

            return market
        else:
            return markets

    def get_market_summaries(self, market_name=None):
        url = self._get_market_summaries(market_name)
        return self._get(url)

    def get_market_history(self, market_name):
        url = self._get_market_history(market_name)
        return self._get(url)

    def get_currencies(self):
        url = self._get_currencies()
        return self._get(url)

    def get_ticker(self, market_name):
        url = self._get_ticker(market_name)
        return self._get(url)

    def get_order_book(self, market_name, order_type='both'):
        url = self._get_order_book(market_name, order_type)
        return self._get(url)

    def buy_limit(self, market_name, quantity, rate):
        url = self._buy_limit(market_name, quantity, rate)
        return self._get(url)

    def sell_limit(self, market_name, quantity, rate):
        url = self._sell_limit(market_name, quantity, rate)
        return self._get(url)

    def cancel_order(self, uuid):
        url = self._cancel_order(uuid)
        return self._get(url)

    def get_open_orders(self, market_name=None):
        url = self._get_open_orders(market_name)
        return self._get(url)

    def get_order(self, uuid):
        url = self._get_order(uuid)
        return self._get(url)

    def get_order_history(self, market_name=None):
        url = self._get_order_history(market_name)
        return self._get(url)

    def get_balances(self, currency=None):
        url = self._get_balances(currency)
        return self._get(url)

    def get_deposit_address(self, currency):
        url = self._get_deposit_address(currency)
        return self._get(url)

    def withdraw(self, currency, quantity, address, payment_id=None):
        url = self._withdraw(currency, quantity, address, payment_id)
        return self._get(url)

    def get_withdrawal_history(self, currency=None):
        url = self._get_withdrawal_history(currency)
        return self._get(url)

    def get_deposit_history(self, currency=None):
        url = self._get_deposit_history(currency)
        return self._get(url)

    def get_candles(self, market_name, tick_interval):
        url = self._get_candles(market_name, tick_interval)
        return self._get(url)

    def get_latest_candle(self, market_name, tick_interval):
        url = self._get_latest_candle(market_name, tick_interval)
        return self._get(url)
