.. :changelog:

Release History
---------------

0.0.4 (2018-03-17)
++++++++++++++++++
- Async get function now catches ClientOSErrors and reraises it as ResponseError

0.0.3 (2018-03-16)
++++++++++++++++++
- ResponseError now returns the full data information

0.0.2 (2018-03-16)
++++++++++++++++++
- Added optional market_name filter to get_markets() function. Note this is not provided by bittrex api, still retrieving all markets in background

0.0.1 (2018-03-16)
++++++++++++++++++

**Initial Release**

- Synchronous and asynchronous endpoints available for all known bittrex API v1.1
- Two basic examples
- Shitty documentation
- No tests
