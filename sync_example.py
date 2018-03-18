#!/usr/bin/env python3

from bittrex import BittrexSession
from bittrex.exceptions import RequestError


def main():
    session = BittrexSession.load_from_file('configs/bittrex.json')

    market_name = 'BTC-LTC'
    currency = 'BTC'
    uuid = 'dummy'

    print('Retrieving markets')
    print('==================')
    markets = session.get_markets()
    print(f'{len(markets)} markets found')
    print(f'First response is {markets[0]}\n\n')

    print('Retrieving market summaries')
    print('===========================')
    market_summaries = session.get_market_summaries()
    print(f'{len(market_summaries)} markets found')
    print(f'First response is: {market_summaries[0]}\n\n')

    print(f'Retrieving {market_name} get_market_history')
    print('=================================')
    market_history = session.get_market_history(market_name)
    print(f'{len(market_history)} found')
    print(f'First response is: {market_history[0]}\n\n')

    print('Retrieving get_currencies')
    print('=========================')
    currencies = session.get_currencies()
    print(f'{len(currencies)} found')
    print(f'First response is: {currencies[0]}\n\n')

    print(f'Retrieving get_ticker for {market_name}')
    print('=========================')
    market_ticker = session.get_ticker(market_name)
    print(f'Response is: {market_ticker}\n\n')

    print('Retrieving get_order_book')
    print('=========================')
    order_book = session.get_order_book(
        market_name,
        'buy'
    )
    print(f'{len(order_book)} found')
    print(f'First response is: {order_book[0]}\n\n')

    print('Retrieving get_open_orders')
    print('==========================')
    open_orders = session.get_open_orders()
    print(f'{len(open_orders)} found')
    if open_orders:
        print(f'First response is: {open_orders[0]}')

    print('\n\nRetrieving get_order_history')
    print('=========================')
    order_history = session.get_order_history()
    print(f'{len(order_history)} found')
    if order_history:
        print(f'First response is: {order_history[0]}')

    print('\n\nRetrieving get_balances')
    print('=========================')
    balances = session.get_balances()
    print(f'{len(balances)} found')
    if balances:
        print(f'First response is: {balances[0]}')

    print('\n\nRetrieving get_deposit_address')
    print('=========================')
    deposit_address = session.get_deposit_address(currency)
    print(f'Response is: {deposit_address}\n\n')

    print('Retrieving get_withdrawal_history')
    print('=========================')
    withdrawal_history = session.get_withdrawal_history()
    print(f'{len(withdrawal_history)} found')
    if withdrawal_history:
        print(f'First response is: {withdrawal_history[0]}')

    print(f'\n\nRetrieving get_order')
    print('=========================')
    try:
        order = session.get_order(uuid)
        print(f'Response is: {order}')
    except RequestError as e:
        print(f'Error retrieving order {uuid}: {e}')

    print('\n\nRetrieving get_deposit_history')
    print('=========================')
    deposit_history = session.get_deposit_history()
    print(f'{len(deposit_history)} found')
    if deposit_history:
        print(f'First response is: {deposit_history[0]}\n\n')

    print('\n\nRetrieving get_candles()')
    print('=========================')
    candles = session.get_candles(market_name, 'five_min')
    print(f'{len(candles)} found')
    if candles:
        print(f'First response is: {candles[0]}\n\n')

    print('\n\nRetrieving get_latest_candle()')
    print('=========================')
    candles = session.get_latest_candle(market_name, 'five_min')
    print(f'{len(candles)} found')
    if candles:
        print(f'First response is: {candles[0]}\n\n')


if __name__ == '__main__':
    main()
