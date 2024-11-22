import requests
import logging

logger = logging.getLogger(__name__)

class DextoolsAPIV2:
    def __init__(self, api_key, useragent="API-Wrapper/0.3", plan="partner"):
        self._api_key = api_key
        self._useragent = useragent
        self.plan = None

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
        logger.debug(f"Plan url: {self.url}")
        logger.info(f"Set up plan: {plan}")

    def get_blockchain(self, chain):
        endpoint = "/blockchain/"
        response = requests.get(self.url + endpoint + chain, headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_blockchains(self, order="asc", sort="name", page=None, pageSize=None):
        endpoint = "/blockchain"
        response = requests.get(self.url + endpoint, params={"order": order, "sort": sort, "page": page, "pageSize": pageSize}, headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_dex_factory_info(self, chain, address):
        endpoint = "/dex/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}", headers=self._headers)
        logger.debug(response.url)
        return response.json()

    def get_dexes(self, chain, order="asc", sort="name", page=None, pageSize=None):
        endpoint = "/dex/"
        response = requests.get(self.url + endpoint + chain, params={"order": order, "sort": sort, "page": page, "pageSize": pageSize}, headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_pool(self, chain, address):
        endpoint = "/pool/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}", headers=self._headers)
        logger.debug(response.url)
        return response.json()

    def get_pool_liquidity(self, chain, address):
        endpoint = "/pool/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/liquidity", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_pool_score(self, chain, address):
        endpoint = "/pool/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/score", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_pool_price(self, chain, address):
        endpoint = "/pool/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/price", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_pool_locks(self, chain, address):
        endpoint = "/pool/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/locks", headers=self._headers)
        logger.debug(response.url)
        return response.json()    

    def get_pools(self, chain, from_, to, order="asc", sort="creationTime", page=None, pageSize=None):
        endpoint = "/pool/"
        response = requests.get(self.url + endpoint + chain, params={"order": order, "sort": sort, "from": from_, "to": to, "page": page, "pageSize": pageSize}, headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token(self, chain, address):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token_locks(self, chain, address):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/locks", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token_score(self, chain, address):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/score", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token_info(self, chain, address):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/info", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token_price(self, chain, address):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/price", headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token_audit(self, chain, address):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/audit", headers=self._headers)
        logger.debug(response.url)
        return response.json()    
    
    def get_tokens(self, chain, from_, to, order="asc", sort="socialsInfoUpdated", page=None, pageSize=None):
        endpoint = "/token/"
        response = requests.get(self.url + endpoint + chain, params={"order": order, "sort": sort, "from": from_, "to": to, "page": page, "pageSize": pageSize}, headers=self._headers)
        logger.debug(response.url)
        return response.json()
    
    def get_token_pools(self, chain, address, from_, to, order="asc", sort="creationTime", page=None, pageSize=None):
        endpoint = "/token/"
        response = requests.get(f"{self.url}{endpoint}{chain}/{address}/pools", params={"order": order, "sort": sort, "from": from_, "to": to, "page": page, "pageSize": pageSize}, headers=self._headers)
        logger.debug(response.url)
        return response.json()

    def get_ranking_hotpools(self, chain):
        endpoint = "/ranking/"
        response = requests.get(f"{self.url}{endpoint}{chain}/hotpools", headers=self._headers)
        logger.debug(response.url)
        return response.json()

    def get_ranking_gainers(self, chain):
        endpoint = "/ranking/"
        response = requests.get(f"{self.url}{endpoint}{chain}/gainers", headers=self._headers)
        logger.debug(response.url)
        return response.json()

    def get_ranking_losers(self, chain):
        endpoint = "/ranking/"
        response = requests.get(f"{self.url}{endpoint}{chain}/losers", headers=self._headers)
        logger.debug(response.url)
        return response.json()