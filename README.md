# DEXTools Python
[![Python application](https://github.com/alb2001/dextools-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/alb2001/dextools-python/actions/workflows/python-app.yml)
[![Downloads](https://static.pepy.tech/badge/dextools-python)](https://pepy.tech/project/dextools-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI](https://img.shields.io/pypi/v/dextools-python)
A simple Python API wrapper for DEXTools

## Installation

```
pip install dextools-python
```

## Obtaining API Key
To obtain an API key, you will need to fill up [this form](https://forms.gle/yviVwKYaqs81BMB77).


## Getting Started
To get started, import the package, and initiate a DextoolsAPI instance object by passing your API key:
```
from dextools_python import DextoolsAPI
dextools = DextoolsAPI(api_key)
```

You can also pass an optional user agent:
```
dextools = DextoolsAPI(api_key, useragent="User-Agent")
```

## Queries
Below are a set of queries supported by the [Dextools API](https://api.dextools.io/docs). All data is returned as a Python dictionary for easy data handling.

### Get pairs of a token
To get the pairs of a token, pass a `chain slug` and a `pair address`:
```
pair = dextools.get_pair("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pair)
```

### Get token details
To get token details, pass a `chain slug`, and a `token address`:
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
To get the exchange list, pass a `chain slug`:
```
exchange_list = dextools.get_exchange_list("ether")
print(exchange_list)
```

You can also pass the `page` and `pageSize` parameters:
```
exchange_list = dextools.get_exchange_list("ether", 1, 50)
print(exchange_list)
```

## Testing
A set of tests have been included inside `tests` folder. You will need to setup an environment variable as `DextoolsAPIKey` with your API key

## Chain slugs
Below is a list of current chain slugs for supported blockhains:
| Blockchain   | ID            |
| ------------ | ------------- |
| ETHEREUM     |  ether        |
| BNB          |  bnb          |
| POLYGON      |  polygon      |
| FANTOM       |  fantom       |
| CRONOS       |  cronos       |
| AVALANCHE    |  avalanche    |
| VELAS        |  velas        |
| OASIS        |  oasis        |
| KUCOIN       |  kucoin       |
| METIS        |  metis        |
| OPTIMISM     |  optimism     |
| ARBITRUM     |  arbitrum     |
| CELO         |  celo         |
| TELOS        |  telos        |
| AURORA       |  aurora       |
| MOONBEAM     |  moonbeam     |
| MOONRIVER    |  moonriver    |
| HARMONY      |  harmony      |
| FUSE         |  fuse         |
| HECO         |  heco         |
| OKC          |  okc          |
| ASTAR        |  astar        |
| KLAYTN       |  klaytn       |
| IOTEX        |  iotex        |
| MILKOMEDA    |  milkomeda    |
| DFK          |  dfk          |
| SOLANA       |  solana       |
| EVMOS        |  evmos        |
| DOGECHAIN    |  dogechain    |
| ETC          |  etc          |
| GNOSIS       |  gnosis       |
| BITGERT      |  bitgert      |
| CANTO        |  canto        |
| FLARE        |  flare        |
| ARBITRUMNOVA |  arbitrumnova |
| REDLIGHT     |  redlight     |
| CONFLUX      |  conflux      |
| SMARTBCH     |  smartbch     |
| KARDIA       |  kardia       |
| TOMB         |  tomb         |
| WAN          |  wan          |
| BOBA         |  boba         |
| ELASTOS      |  elastos      |
| NOVA         |  nova         |
| HOO          |  hoo          |
| SHIDEN       |  shiden       |
| FUSION       |  fusion       |
| RSK          |  rsk          |
| CUBE         |  cube         |
| SYSCOIN      |  syscoin      |
| KAVA         |  kava         |
| THUNDERCORE  |  thundercore  |
| ECHELON      |  echelon      |
| METER        |  meter        |
| KEK          |  kek          |
| TOMO         |  tomo         |
| RONIN        |  ronin        |
| SHIB         |  shib         |
| ETHW         |  ethw         |
| ETHF         |  ethf         |
| MUU          |  muu          |
| SX           |  sx           |
| ALVEY        |  alvey        |
| APTOS        |  aptos        |
| MULTIVERSX   |  multiversx   |
| ProofOfMemes |  pom          |
| EXOSAMA      |  exosama      |
| ENERGI       |  energi       |
| GOERLI       |  ethergoerli  |
| CORE DAO     |  coredao      |

## Authors
* [alb2001](https://github.com/alb2001)


## More information
* [dextools-python on PyPI](https://pypi.org/project/dextools-python)
* [DEXTools](https://www.dextools.io)
* [Dextools API](https://api.dextools.io/docs)
* [Request API Key](https://forms.gle/yviVwKYaqs81BMB77)