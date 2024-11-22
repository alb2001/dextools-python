![Image](https://raw.githubusercontent.com/alb2001/dextools-python/master/assets/dextools-python.png)

# DEXTools Python
[![Python application](https://github.com/alb2001/dextools-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/alb2001/dextools-python/actions/workflows/python-app.yml)
[![Downloads](https://static.pepy.tech/badge/dextools-python)](https://pepy.tech/project/dextools-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/dextools-python)](https://pypi.org/project/dextools-python/)

A simple Python API wrapper for DEXTools.
Supports [Dextools API v1](https://api.dextools.io/docs) and [Dextools API v2](https://developer.dextools.io/docs/start)

1. [Installation](#installation)
2. [Obtaining API Key](#obtaining-api-key)
3. [Getting Started](#getting-started)
    1. [Version 1](#version-1)
    2. [Version 2](#version-2)
        1. [Available plans - Setting your plan](#available-plans---setting-your-plan)
4. [Version 1 Queries](#version-1-queries)
    1. [Get pairs of a token](#get-pairs-of-a-token)
    2. [Get token details](#get-token-details)
    3. [Get chain list](#get-chain-list)
    4. [Get exchange list](#get-exchange-list)
5. [Version 2 Queries](#version-2-queries)
    1. [Blockchain](#blockchain)
        1. [Get blockchain info](#get-blockchain-info)
        2. [Get blockchains sorted by default settings](#get-blockchains-sorted-by-default-settings)
        3. [Get blockchains sorted by default settings and descending order](#get-blockchains-sorted-by-default-settings-and-descending-order)
    2. [Exchange](#exchange)
        1. [Get dex factory info](#get-dex-factory-info)
        2. [Get dexes on a specific chain](#get-dexes-on-a-specific-chain)
        3. [Get dexes on a specific chain sorted by name and descending order](#get-dexes-on-a-specific-chain-sorted-by-name-and-descending-order)
    3. [Pool](#pool)
        1. [Get pool info](#get-pool-info)
        2. [Get pool liquidity](#get-pool-liquidity)
        3. [Get pool score](#get-pool-score)
        4. [Get pool price](#get-pool-price)
        5. [Get pool locks](#get-pool-locks)
        6. [Get pools](#get-pools)
        7. [Get pools sorted by `creationBlock` and descending order and providing block numbers instead](#get-pools-sorted-by-creationblock-and-descending-order-and-providing-block-numbers-instead)
    4. [Token](#token)
        1. [Get token](#get-token)
        2. [Get token locks](#get-token-locks)
        3. [Get token score](#get-token-score)
        4. [Get token info](#get-token-info)
        5. [Get token price](#get-token-price)
        6. [Get token price](#get-token-audit)
        7. [Get tokens](#get-tokens)
        8. [Get tokens sorted by `creationBlock` and descending order and providing block numbers instead in descending order](#get-tokens-sorted-by-creationblock-and-descending-order-and-providing-block-numbers-instead-in-descending-order)
        8. [Get tokens sorted by `socialsInfoUpdated` and descending order and datetimes in descending order](#get-tokens-sorted-by-socialsinfoupdated-and-descending-order-and-datetimes-in-descending-order)
        9. [Get token pools](#get-token-pools)
        10. [Get token pools sorted by `creationBlock` and descending order and providing block numbers instead in descending order](#get-token-pools-sorted-by-creationblock-and-descending-order-and-providing-block-numbers-instead-in-descending-order)
    5. [Rankings](#rankings)
        1. [Get hot pools](#get-hot-pools)
        2. [Get gainers](#get-gainers)
        3. [Get losers](#get-losers)
6. [Page and PageSize arguments](#page-and-pagesize-arguments)
7. [Asynchronous support with asyncio](#asynchronous-support-with-asyncio)
8. [Examples](#examples)
9. [Testing](#testing)
10. [Supported Blockchains](#supported-blockchains)
11. [Authors](#authors)
12. [More information](#more-information)


## Installation

```
pip install dextools-python
```

## Obtaining API Key
To obtain an API key, head to the [Developer Portal](https://developer.dextools.io/) and choose your plan.


## Getting Started
There are 2 versions of the Dextools API. [Dextools API v1](https://api.dextools.io/docs) and [Dextools API v2](https://developer.dextools.io/docs/start)

### Version 1
To get started, import the package, and initiate a `DextoolsAPI` instance object by passing your API key:
```
from dextools_python import DextoolsAPI
dextools = DextoolsAPI(api_key)
```

You can also pass an optional user agent:
```
dextools = DextoolsAPI(api_key, useragent="User-Agent")
```

### Version 2
To get started, import the package, and initiate a `DextoolsAPIV2` instance object by passing your API key and your plan:
```
from dextools_python import DextoolsAPIV2
dextools = DextoolsAPIV2(api_key, plan="trial")
```

You can also pass an optional user agent:
```
dextools = DextoolsAPIV2(api_key, useragent="User-Agent", plan="trial")
```

If you don't specify any plan when instantiating the object, it will default to "partner" plan

#### Available plans - Setting your plan
You can setup your plan when setting the object instance by providing the `plan` argument in the constructor. If no `plan` is specified, it will default to "partner" plan

To set your plan after the object is created, you can use the `set_plan("your_plan")` method
```
dextools.set_plan("standard")
```

Available values: `"free"`, `"trial"`, `"standard"`, `"advanced"`, `"pro"`, and `"partner"`


## Version 1 Queries
Below are a set of queries supported by the [Dextools API v1](https://api.dextools.io/docs). All data is returned as a Python dictionary for easy data handling.

### Get pairs of a token
To get the pairs of a token, pass a `chain id` and a `pair address`:
```
pair = dextools.get_pair("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pair)
```

### Get token details
To get token details, pass a `chain id`, and a `token address`:
```
token = dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token)
```

You can also pass the `page` and `pageSize` parameters:
```
token = dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", 1, 50)
print(token)
```

### Get chain list
To get the chain list:
```
chain_list = dextools.get_chain_list()
print(chain_list)
```

You can also pass the `page` and `pageSize` parameters:
```
chain_list = dextools.get_chain_list(1, 50)
print(chain_list)
```

### Get exchange list
To get the exchange list, pass a `chain id`:
```
exchange_list = dextools.get_exchange_list("ether")
print(exchange_list)
```

You can also pass the `page` and `pageSize` parameters:
```
exchange_list = dextools.get_exchange_list("ether", 1, 50)
print(exchange_list)
```

## Version 2 Queries
Below are a set of queries supported by the [Dextools API v2](https://developer.dextools.io/docs/start). All data is returned as a Python dictionary for easy data handling.

### Blockchain
#### Get blockchain info
```
blockchain = dextools.get_blockchain("ether")
print(blockchain)
```

#### Get blockchains sorted by default settings
```
blockchains = dextools.get_blockchains()
print(blockchains)
```

#### Get blockchains sorted by default settings and descending order
```
blockchains = dextools.get_blockchains(sort="name", order="desc")
print(blockchains)
```

### Exchange
#### Get dex factory info
```
factory = dextools.get_dex_factory_info("ether", "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
print(factory)
```

#### Get dexes on a specific chain
```
dexes = dextools.get_dexes("ether")
print(dexes)
```

#### Get dexes on a specific chain sorted by name and descending order
```
dexes = dextools.get_dexes("ether", sort="creationBlock", order="desc")
print(dexes)
```

### Pool
#### Get pool info
```
pool = dextools.get_pool("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pool)
```

#### Get pool liquidity
```
pool_liquidity = dextools.get_pool_liquidity("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pool_liquidity)
```

#### Get pool score
```
pool_score = dextools.get_pool_score("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pool_score)
```

#### Get pool price
```
pool_price = dextools.get_pool_price("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pool_price)
```

#### Get pool locks
```
pool_locks = dextools.get_pool_locks("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pool_locks)
```

#### Get pools
```
pools = dextools.get_pools("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
print(pools)
```

#### Get pools sorted by `creationBlock` and descending order and providing block numbers instead
```
pools = dextools.get_pools("ether", from_="12755070", to="12755071", sort="creationBlock", order="desc")
print(pools)
```

### Token
#### Get token
```
token = dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token)
```

#### Get token locks
```
token_locks = dextools.get_token_locks("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token_locks)
```

#### Get token score
```
token_score = dextools.get_token_score("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token_score)
```

#### Get token info
```
token_info = dextools.get_token_info("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token_info)
```

#### Get token price
```
token_price = dextools.get_token_price("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token_price)
```

#### Get token audit
```
token_audit = dextools.get_token_audit("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token_audit)
```

#### Get tokens
```
tokens = dextools.get_tokens("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
print(tokens)
```

#### Get tokens sorted by `creationBlock` and descending order and providing block numbers instead in descending order
```
tokens = dextools.get_tokens("ether", from_="18570000", to="18570500", sort="creationBlock", order="desc")
print(tokens)
```

#### Get tokens sorted by `socialsInfoUpdated` and descending order and datetimes in descending order
```
tokens = dextools.get_tokens("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00", sort="socialsInfoUpdated", order="desc")
print(tokens)
```

#### Get token pools
```
token_pools = dextools.get_token_pools("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
print(token_pools)
```

#### Get token pools sorted by `creationBlock` and descending order and providing block numbers instead in descending order
```
token_pools = dextools.get_token_pools("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", from_="18570000", to="18570500", sort="creationBlock", order="desc")
print(token_pools)
```

### Rankings
#### Get hot pools
```
hot_pools = dextools.get_ranking_hotpools("ether")
print(hot_pools)
```

#### Get gainers
```
gainers = dextools.get_ranking_gainers("ether")
print(gainers)
```

#### Get losers
```
losers = dextools.get_ranking_losers("ether")
print(losers)
```

## Page and PageSize arguments
Some methods support the `page` and `pageSize` arguments. Check out the API documentation for more information.

## Asynchronous support with asyncio
Asynchronous support has been added through [asyncio](https://docs.python.org/3/library/asyncio.html).
You can initiate an `AsyncDextoolsAPI` instance for API version 1, or an `AsyncDextoolsAPIV2` instance for API version 2.

Through a context manager (session will close automatically when the context manager ends):
```
import asyncio
from dextools_python import AsyncDextoolsAPIV2

api_key = "YOUR_API_KEY"

async def main():
    async with AsyncDextoolsAPIV2(api_key, plan="partner") as dextools:
        response = await dextools.get_blockchains()
        print(response)

asyncio.run(main())
```

Creating an instance and then closing the session explicitly at the end:
```
import asyncio
from dextools_python import AsyncDextoolsAPIV2

api_key = "YOUR_API_KEY"

async def main():
    dextools = AsyncDextoolsAPIV2(api_key, plan="partner")

    response = await dextools.get_blockchains()
    print(response)

    await dextools.close()

asyncio.run(main())
```

## Examples
Check out the `examples` folder for some synchronous and asynchronous example scripts.

## Testing
A set of tests have been included inside `tests` folder. You will need to set an environment variable as `DextoolsAPIKey` using your API key.

## Supported Blockchains
Dextools adds support for new blockchains from time to time. `dextools.get_blockchains()` to get a list of supported blockchains and their IDs

## Authors
* [alb2001](https://github.com/alb2001)


## More information
* [dextools-python on PyPI](https://pypi.org/project/dextools-python)
* [DEXTools](https://www.dextools.io)
* [Dextools API v1](https://api.dextools.io/docs)
* [Dextools API v2](https://developer.dextools.io/docs/start)
* [Developer Portal](https://developer.dextools.io/)
* [asyncio](https://docs.python.org/3/library/asyncio.html)