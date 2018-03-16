bittrex-python
==============
A Python => 3.6 wrapper around the bittrex API with sync- and asynchronous interfaces 


Disclaimer
----------
*WARNING* DO NOT USE THIS LIBRARY! Built this for myself and not using it to trade anything with it. No proper tests are present, not intending to maintain this library much, just a personal experiment.

Did I mention you shouldn't use this library?

Description
-----------
This library provides a python wrapper around the bittrex api v1.1. I've tried to seperate the API endpoint parsing from the actual http requests to provide both a synchronous (using requests) and asynchronous (using aiohttp) interface.


Installation
------------
Have to pull code from the github repo for the moment. Not sure if i'll submit package to Pypi in the future.

After pulling the repo you can install using:
```
python3 setup.py install
```

Don't do this though, use pipenv, thats what all the cool kids are doing nowadays

synchronous library depends on having requests module installed. To use the asynchronous library, make sure aiohttp is installed as well.

Compatibility
-------------
You will need to be running at least python v3.6 cause I LOVE using f-strings. You should love them too...!

Coffee
------
If you'd like to buy me a coffee, donations are always welcome! Not sure why you'd want to through since YOU SHOULD NOT USE THIS LIBRARY!
BTC address: 1G5MHp74SY7pdEWS4HfeBJuaRkXG6p6XKi
LTC address: 
