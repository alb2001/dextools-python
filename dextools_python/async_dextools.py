import asyncio
import aiohttp


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
            return await response.json()
    
    async def get_token(self, chain, address, page=None, pageSize=None):
        endpoint = "/token"

        async with self._session.get(self.url + endpoint, params=self.params({"chain": chain, "address": address, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()        
    
    async def get_chain_list(self, page=None, pageSize=None):
        endpoint = "/chain/list"

        async with self._session.get(self.url + endpoint, params=self.params({"page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()
    
    async def get_exchange_list(self, chain, page=None, pageSize=None):
        endpoint = "/exchange/list"

        async with self._session.get(self.url + endpoint, params=self.params({"chain": chain, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()
        
    def params(self, params):
        my_params = {}
        for k, v in params.items():
            if v is not None:
                my_params[k] = v
        return my_params


class AsyncDextoolsAPIV2:
    def __init__(self, api_key, useragent="API-Wrapper/0.3", plan="partner"):
        self._api_key = api_key
        self._useragent = useragent
        self.plan = None
        self._session = aiohttp.ClientSession()

        self.set_plan(plan)

    def set_plan(self, plan):
        # python versions older than 3.10 don't support switch/case statements, using if elif instead
        plan = plan.lower()
        plans = ["free", "trial", "standard", "advanced", "pro"]
        if plan in plans:
            self.plan = plan
            self.url = f"http://public-api.dextools.io/{plan}/v2"
            self._headers = {"X-API-Key": self._api_key, "accept": "application/json", "User-Agent": self._useragent}
        elif plan == "partner":
            self.plan = plan
            self.url = f"https://api.dextools.io/v2"
            self._headers = {"X-API-Key": self._api_key, "accept": "application/json", "User-Agent": self._useragent}
        else:
            raise Exception("Plan not found")
    
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self._session.close()

    async def get_blockchain(self, chain):
        endpoint = "/blockchain/"

        async with self._session.get(self.url + endpoint + chain, headers=self._headers) as response:
            return await response.json()
    
    async def get_blockchains(self, order="asc", sort="name", page=None, pageSize=None):
        endpoint = "/blockchain"

        async with self._session.get(self.url + endpoint, params=self.params({"order": order, "sort": sort, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()
    
    async def get_dex_factory_info(self, chain, address):
        endpoint = "/dex/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}", headers=self._headers) as response:
            return await response.json()

    async def get_dexes(self, chain, order="asc", sort="name", page=None, pageSize=None):
        endpoint = "/dex/"
        async with self._session.get(self.url + endpoint + chain, params=self.params({"order": order, "sort": sort, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()
    
    async def get_pool(self, chain, address):
        endpoint = "/pool/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}", headers=self._headers) as response:
            return await response.json()

    async def get_pool_liquidity(self, chain, address):
        endpoint = "/pool/"
        
        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/liquidity", headers=self._headers) as response:
            return await response.json()
    
    async def get_pool_score(self, chain, address):
        endpoint = "/pool/"
        
        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/score", headers=self._headers) as response:
            return await response.json()
    
    async def get_pool_price(self, chain, address):
        endpoint = "/pool/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/price", headers=self._headers) as response:
            return await response.json()

    async def get_pools(self, chain, from_, to, order="asc", sort="creationTime", page=None, pageSize=None):
        endpoint = "/pool/"
        
        async with self._session.get(self.url + endpoint + chain, params=self.params({"order": order, "sort": sort, "from": from_, "to": to, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()
    
    async def get_token(self, chain, address):
        endpoint = "/token/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}", headers=self._headers) as response:
            return await response.json()
    
    async def get_token_locks(self, chain, address):
        endpoint = "/token/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/locks", headers=self._headers) as response:
            return await response.json()
    
    async def get_token_score(self, chain, address):
        endpoint = "/token/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/score", headers=self._headers) as response:
            return await response.json()
    
    async def get_token_info(self, chain, address):
        endpoint = "/token/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/info", headers=self._headers) as response:
            return await response.json()
    
    async def get_token_price(self, chain, address):
        endpoint = "/token/"
        
        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/price", headers=self._headers) as response:
            return await response.json()
    
    async def get_tokens(self, chain, from_, to, order="asc", sort="socialsInfoUpdated", page=None, pageSize=None):
        endpoint = "/token/"
        
        async with self._session.get(self.url + endpoint + chain, params=self.params({"order": order, "sort": sort, "from": from_, "to": to, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()
    
    async def get_token_pools(self, chain, address, from_, to, order="asc", sort="creationTime", page=None, pageSize=None):
        endpoint = "/token/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/{address}/pools", params=self.params({"order": order, "sort": sort, "from": from_, "to": to, "page": page, "pageSize": pageSize}), headers=self._headers) as response:
            return await response.json()

    async def get_ranking_hotpools(self, chain):
        endpoint = "/ranking/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/hotpools", headers=self._headers) as response:
            return await response.json()

    async def get_ranking_gainers(self, chain):
        endpoint = "/ranking/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/gainers", headers=self._headers) as response:
            return await response.json()

    async def get_ranking_losers(self, chain):
        endpoint = "/ranking/"

        async with self._session.get(f"{self.url}{endpoint}{chain}/losers", headers=self._headers) as response:
            return await response.json()
    
    def params(self, params):
        my_params = {}
        for k, v in params.items():
            if v is not None:
                my_params[k] = v
        return my_params