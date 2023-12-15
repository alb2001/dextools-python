from dextools_python import DextoolsAPIV2
import pytest
import os


API_KEY = os.getenv("DextoolsAPIKey")


@pytest.fixture
def dextools_instance():
    dextools = DextoolsAPIV2(API_KEY)
    return dextools

def test_get_blockchain(dextools_instance):
    chain = "ether"
    response = dextools_instance.get_blockchain(chain)

    assert response["statusCode"] == 200
    assert response["data"]["id"] == chain
    assert isinstance(response, dict)

def test_get_blockchains(dextools_instance):
    response = dextools_instance.get_blockchains()

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"]["results"], list)

def test_get_dex_factory_info(dextools_instance):
    chain = "ether"
    factory = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
    response = dextools_instance.get_dex_factory_info(chain, factory)
    
    assert response["statusCode"] == 200
    assert response["data"]["factory"] == factory.lower()
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)

def test_get_dexes(dextools_instance):
    chain = "ether"
    response = dextools_instance.get_dexes(chain)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["results"], list)

def test_get_pool(dextools_instance):
    chain = "ether"
    pool = "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d"
    name = "DEXTools"
    symbol = "DEXT"
    address = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    response = dextools_instance.get_pool(chain, pool)

    assert response["statusCode"] == 200
    assert response["data"]["mainToken"]["name"] == name
    assert response["data"]["mainToken"]["symbol"] == symbol
    assert response["data"]["mainToken"]["address"] == address.lower()
    assert isinstance(response, dict)

def test_get_pool_liquidity(dextools_instance):
    chain = "ether"
    pool = "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d"
    response = dextools_instance.get_pool_liquidity(chain, pool)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["reserves"], dict)

def test_get_pool_score(dextools_instance):
    chain = "ether"
    pool = "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d"
    response = dextools_instance.get_pool_score(chain, pool)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["votes"], dict)
    assert isinstance(response["data"]["dextScore"], dict)

def test_get_pool_price(dextools_instance):
    chain = "ether"
    pool = "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d"
    response = dextools_instance.get_pool_price(chain, pool)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)

def test_get_pools_sorted_by_creationTime(dextools_instance):
    chain = "ether"
    from_ = "2023-11-14T19:00:00"
    to = "2023-11-14T23:00:00"
    response = dextools_instance.get_pools(chain, from_, to)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["results"], list)

def test_get_pools_sorted_by_creationBlock(dextools_instance):
    chain = "ether"
    from_ = "12755070"
    to = "12755071"
    sort="creationBlock"
    name = "DEXTools"
    symbol = "DEXT"
    address = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    response = dextools_instance.get_pools(chain, from_, to, sort=sort)

    assert response["statusCode"] == 200
    assert response["data"]["results"][0]["creationBlock"] == int(from_)
    assert response["data"]["results"][0]["mainToken"]["address"] == address
    assert response["data"]["results"][0]["mainToken"]["name"] == name
    assert response["data"]["results"][0]["mainToken"]["symbol"] == symbol
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["results"], list)

def test_get_token(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    name = "DEXTools"
    symbol = "DEXT"
    response = dextools_instance.get_token(chain, token)

    assert response["statusCode"] == 200
    assert response["data"]["address"] == token.lower()
    assert response["data"]["name"] == name
    assert response["data"]["symbol"] == symbol
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)

def test_get_token_locks(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    response = dextools_instance.get_token_locks(chain, token)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)

def test_get_token_score(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    response = dextools_instance.get_token_score(chain, token)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["dextScore"], dict)

def test_get_token_info(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    response = dextools_instance.get_token_info(chain, token)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)

def test_get_token_price(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    response = dextools_instance.get_token_price(chain, token)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)

def test_get_tokens(dextools_instance):
    chain = "ether"
    from_ = "2023-11-14T19:00:00"
    to = "2023-11-14T23:00:00"
    response = dextools_instance.get_tokens(chain, from_, to)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["tokens"], list)

def test_get_tokens_sorted_by_creationBlock(dextools_instance):
    chain = "ether"
    from_ ="18570000"
    to ="18570500"
    sort = "creationBlock"
    response = dextools_instance.get_tokens(chain, from_, to, sort=sort)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["tokens"], list)

def test_get_tokens_sorted_by_socialsInfoUpdated(dextools_instance):
    chain = "ether"
    from_ = "2023-11-14T19:00:00"
    to = "2023-11-14T23:00:00"
    sort = "socialsInfoUpdated"
    response = dextools_instance.get_tokens(chain, from_, to, sort=sort)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["tokens"], list)

def test_get_token_pools(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    from_ = "2023-11-14T19:00:00"
    to = "2023-11-14T23:00:00"
    response = dextools_instance.get_token_pools(chain, token, from_, to)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["results"], list)

def test_get_token_pools_sorted_by_creationBlock(dextools_instance):
    chain = "ether"
    token = "0xfb7b4564402e5500db5bb6d63ae671302777c75a"
    from_ = "18570000"
    to = "18570500"
    sort = "creationBlock"
    response = dextools_instance.get_token_pools(chain, token, from_, to, sort=sort)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["results"], list)

def test_get_ranking_hotpools(dextools_instance):
    chain = "ether"
    response = dextools_instance.get_ranking_hotpools(chain)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)

def test_get_ranking_gainers(dextools_instance):
    chain = "ether"
    response = dextools_instance.get_ranking_gainers(chain)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)

def test_get_ranking_losers(dextools_instance):
    chain = "ether"
    response = dextools_instance.get_ranking_losers(chain)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)

def test_plans(dextools_instance):
    plans = ["free", "standard", "advanced", "pro"]
    for plan in plans:
        dextools_instance.set_plan(plan)
        assert dextools_instance.url == f"https://open-api.dextools.io/{plan}"
        assert dextools_instance._headers.get("X-BLOBR-KEY") == API_KEY

    dextools_instance.set_plan("partner")
    assert dextools_instance.url == f"https://api.dextools.io/v2"
    assert dextools_instance._headers.get("X-API-Key") == API_KEY

    with pytest.raises(Exception) as excinfo:
        dextools_instance.set_plan("Invalid plan")
    assert str(excinfo.value) == "Plan not found"