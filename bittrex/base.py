from urllib.parse import urlencode
import json
from .response import Response
from .exceptions import RequestError, ResponseError
import hashlib
import hmac
from time import time


__version__ = 'v0.0.2'

class BittrexBaseSession:
    def __init__(self, key, secret, host='bittrex.com', version='v1.1', loop=None):
        self.key = key
        self.secret = secret
        self.host = host
        self.version = version

    @property
    def base_url(self):
        return f'https://{self.host}/api/{self.version}/'

    @property
    def nonce(self):
        """Returns the current nonce for apikey signing"""
        return f"{int(time() * 1000)}"

    def _sign_url(self, url):
        """Signs a url with hmac"""
        return hmac.new(
            self.secret.encode(),
            url.encode(),
            hashlib.sha512
        ).hexdigest()

    def _url(self, method, parameters=None):
        """Compile url"""
        url = f'{self.base_url}{method}'

        if parameters is not None:
            encoded_params = urlencode(parameters)
            url += f'?{encoded_params}'

        return url

    def _get(self):
        """Ensure to implement the Async and Sync version"""
        raise NotImplemented

    def _parse_response(self, data):
        """parse the received json response"""

        if data['success'] is False:
            raise RequestError(data['message'])

        if isinstance(data['result'], list):
            return [Response(**result) for result in data['result']]
        elif isinstance(data['result'], dict):
            return Response(**data['result'])
        else:

            raise ResponseError(f"Parsing failed: {data['result']}")

    def _get_markets(self):
        """Retrieve public markets"""
        return self._url('public/getmarkets')

    def _get_market_summaries(self, market_name=None):
        """Retrieve last 24h public active market summaries

        :param market_name: If provided, return summary of specific market
        """
        if market_name is None:
            return self._url('public/getmarketsummaries')
        else:
            params = {'market': market_name}
            return self._url('public/getmarketsummary', params)

    def _get_market_history(self, market_name):
        """Retrieve the latest trades that occured for given market

        :param market_name: Name of the market
        """
        return self._url('public/getmarkethistory', {'market': market_name})

    def _get_currencies(self):
        """Retrieve public currencies"""
        return self._url('public/getcurrencies')

    def _get_ticker(self, market_name):
        """Retrieve current ticker for given market_name"""
        return self._url('public/getticker', {'market': market_name})

    def _get_order_book(self, market_name, order_type='both'):
        """Retrieve orderbook of given market

        :param market_name: short name of Market
        :param order_type: buy, sell or both
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'market': market_name,
            'type': order_type
        }
        return self._url('public/getorderbook', params)

    def _buy_limit(self, market_name, quantity, rate):
        """Used to place a buy order in a specific market. Use buylimit to place
        limit orders.

        :param market_name: Name of the market
        :param quantity (float): amount to purchase
        :param rate (float): rate at which to place the order
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'market': market_name,
            'quantity': quantity,
            'rate': rate
        }
        return self._url('market/buylimit', params)

    def _sell_limit(self, market_name, quantity, rate):
        """Used to place a sell order in a specific market. Use selllimit to place
        limit orders.

        :param market_name: Name of the market
        :param quantity (float): amount to purchase
        :param rate (float): rate at which to place the order
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'market': market_name,
            'quantity': quantity,
            'rate': rate
        }
        return self._url('market/selllimit', params)

    def _cancel_order(self, uuid):
        """Used to cancel a buy or sell order."""
        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'uuid': uuid
        }
        return self._url('market/cancel', params)

    def _get_open_orders(self, market_name=None):
        """Get all orders that you currently have opened.

        :param market_name: Optional limit to specific market
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce
        }

        if market_name is not None:
            params['market'] = market_name

        return self._url('market/getopenorders', params)

    def _get_order(self, uuid):
        """Get single order by uuid

        :param uuid: uuid of specific order
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'uuid': uuid
        }
        return self._url('account/getorder', params)

    def _get_order_history(self, market_name=None):
        """Retrieve your order history"""
        params = {
            'apikey': self.key,
            'nonce': self.nonce
        }
        if market_name is not None:
            params['market'] = market_name

        return self._url('account/getorderhistory', params)

    def _get_balances(self, currency=None):
        """Used to retrieve all balances from your account

        :param currency: optional limit to specific currency, eg. 'LTC'
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce
        }

        if currency is not None:
            params['currency'] = currency
            return self._url('account/getbalance', params)

        return self._url('account/getbalances', params)

    def _get_deposit_address(self, currency):
        """Used to retrieve or generate an address for a specific currency.
        If one does not exist, the call will fail and return ADDRESS_GENERATING
        until one is available.

        :param currency: currency string literal, eg. 'BTC'
        """

        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'currency': currency
        }
        return self._url('account/getdepositaddress', params)

    def _withdraw(self, currency, quantity, address, payment_id=None):
        """Used to withdraw funds from your account. note: please account for txfee.

        :param currency: a string literal for the currency (ie. BTC)
        :param quantity: the quantity of coins to withdraw
        :param address: the address where to send the funds.

        :param paymentid: used for CryptoNotes/BitShareX/Nxt (memo/paymentid)
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce,
            'currency': currency,
            'quantity': quantity,
            'address': address
        }

        if payment_id is not None:
            params['paymentid'] = payment_id

        return self._url('account/withdraw', params)

    def _get_withdrawal_history(self, currency=None):
        """Retrieve your withdrawal history

        :param currency: Optional limit on currency type, eg. 'BTC'
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce
        }

        if currency is not None:
            params['currency'] = currency

        return self._url('account/getwithdrawalhistory', params)

    def _get_deposit_history(self, currency=None):
        """Retrieve your deposit history

        :param currency: Optional limit on currency type, eg. 'BTC'
        """
        params = {
            'apikey': self.key,
            'nonce': self.nonce
        }
        if currency is not None:
            params['currency'] = currency

        return self._url('account/getdeposithistory', params)

    @classmethod
    def load_from_file(cls, filename, loop=None):
        """Initialise class through config file"""

        with open(filename, 'r') as f:
            config = json.load(f)

        key = config['key']
        secret = config['secret']
        version = config.get('version', 'v1.1')

        return cls(key, secret, version=version, loop=loop)
