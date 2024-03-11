import asyncio
import aiohttp
import logging

logger = logging.getLogger(__name__)

class AsyncDextoolsAPI:
    def __init__(self, api_key, useragent="API-Wrapper/0.3"):
        self.url = f"https://api.dextools.io/v1"
        self._api_key = api_key
        self._useragent = useragent
        self._headers = {"X-API-Key": self._api_key, "accept": "application/json", "User-Agent": self._useragent}
        self._session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self._session.close()

    async def get_pair(self, chain, address):
        endpoint = "/pair"

        async with self._session.get(self.url + endpoint, params={"chain": chain, "address": address}, headers=self._headers) as response:
            logger.debug(response.url)
            return await response.json()
    
    async def get_token(self, chain, address, page=None, pageSize=None):
        endpoint = "/token"

        async with self._session.get(self.url + endpoint, params=self.params({"chain": chain, "address": address, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            logger.debug(response.url)
            return await response.json()        
    
    async def get_chain_list(self, page=None, pageSize=None):
        endpoint = "/chain/list"

        async with self._session.get(self.url + endpoint, params=self.params({"page": page, "pageSize": pageSize}), headers=self._headers) as response:
            logger.debug(response.url)
            return await response.json()
    
    async def get_exchange_list(self, chain, page=None, pageSize=None):
        endpoint = "/exchange/list"

        async with self._session.get(self.url + endpoint, params=self.params({"chain": chain, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            logger.debug(response.url)
            return await response.json()
        
    def params(self, params):
        my_params = {}
        for k, v in params.items():
            if v is not None:
                my_params[k] = v
        return my_params
