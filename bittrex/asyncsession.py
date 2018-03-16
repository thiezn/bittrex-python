from .base import BittrexBaseSession
import requests
from .exceptions import ResponseError

try:
    import aiohttp
except ModuleNotFoundError:
    # Note: Async Bittrex client not available
    pass


class BittrexAsyncSession(BittrexBaseSession):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = aiohttp.ClientSession(loop=kwargs['loop'])

    # NOTE: We need to properly close off the ClientSession().
    # The aiohttp developer mentioned best way is to register
    # an on_cleanup signal: https://github.com/aio-libs/aiohttp/issues/789
    # when using this in combination with aiohttp server

    async def close(self):
        await self.session.close()

    async def _get(self, url, payload=None):
        """async HTTP GET request"""

        headers = {'apisign': self._sign_url(url)}
        async with self.session.get(
            url, json=payload, headers=headers
        ) as response:
            if response.status != requests.codes.ok:
                raise ResponseError(f'{url} {response.status}')

            json_response = await response.json()

        return self._parse_response(json_response)

    async def get_markets(self):
        url = self._get_markets()
        return await self._get(url)

    async def get_market_summaries(self, market_name=None):
        url = self._get_market_summaries(market_name)
        return await self._get(url)

    async def get_market_history(self, market_name):
        url = self._get_market_history(market_name)
        return await self._get(url)

    async def get_currencies(self):
        url = self._get_currencies()
        return await self._get(url)

    async def get_ticker(self, market_name):
        url = self._get_ticker(market_name)
        return await self._get(url)

    async def get_order_book(self, market_name, order_type='both'):
        url = self._get_order_book(market_name, order_type)
        return await self._get(url)

    async def buy_limit(self, market_name, quantity, rate):
        url = self._buy_limit(market_name, quantity, rate)
        return await self._get(url)

    async def sell_limit(self, market_name, quantity, rate):
        url = self._sell_limit(market_name, quantity, rate)
        return await self._get(url)

    async def cancel_order(self, uuid):
        url = self._cancel_order(uuid)
        return await self._get(url)

    async def get_open_orders(self, market_name=None):
        url = self._get_open_orders(market_name)
        return await self._get(url)

    async def get_order(self, uuid):
        url = self._get_order(uuid)
        return await self._get(url)

    async def get_order_history(self, market_name=None):
        url = self._get_order_history(market_name)
        return await self._get(url)

    async def get_balances(self, currency=None):
        url = self._get_balances(currency)
        return await self._get(url)

    async def get_deposit_address(self, currency):
        url = self._get_deposit_address(currency)
        return await self._get(url)

    async def withdraw(self, currency, quantity, address, payment_id=None):
        url = self._withdraw(currency, quantity, address, payment_id)
        return await self._get(url)

    async def get_withdrawal_history(self, currency=None):
        url = self._get_withdrawal_history(currency)
        return await self._get(url)

    async def get_deposit_history(self, currency=None):
        url = self._get_deposit_history(currency)
        return await self._get(url)
