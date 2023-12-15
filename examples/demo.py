from dextools_python import DextoolsAPI

api_key = "YOUR_API_KEY"


# Initiate DextoolsAPI instance object by passing your "API Key":
dextools = DextoolsAPI(api_key)

# Initiate DextoolsAPI instance object by passing your "API Key", and an optional "User Agent":
dextools = DextoolsAPI(api_key, useragent="User-Agent")

# Setting your plan after creating the object
dextools.set_plan("partner")


# Get pair of a token, pass a "chain slug" and a "pair address":
pair = dextools.get_pair("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
print(pair)


# Get token details, pass a "chain slug", and a "token address":
token = dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
print(token)


# Get token details, pass a "chain slug", "token address", and optional "page" and "pageSize" parameters:
token = dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", 1, 50)
print(token)


# Get chain list:
chain_list = dextools.get_chain_list()
print(chain_list)


# Get chain list, passing optional "page" and "pageSize" parameters:
chain_list = dextools.get_chain_list(1, 50)
print(chain_list)


# Get exchange list, passing a "chain slug":
exchange_list = dextools.get_exchange_list("ether")
print(exchange_list)


# Get exchange list, passing a "chain slug", passing optional "page" and "pageSize" parameters:
exchange_list = dextools.get_exchange_list("ether", 1, 50)
print(exchange_list)