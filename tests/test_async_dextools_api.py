from dextools_python import AsyncDextoolsAPI
import pytest
import pytest_asyncio
import os


API_KEY = os.getenv("DextoolsAPIKey")


@pytest_asyncio.fixture
async def dextools_instance():
    dextools_instance = AsyncDextoolsAPI(API_KEY)
    yield dextools_instance
    await dextools_instance.close()

@pytest.mark.asyncio
async def test_get_pair_success(dextools_instance):
    print(dextools_instance._api_key)
    chain = "ether"
    pair = "0x9d378c90057bb8f5b7f1a39e55091bb078cd5974"
    response = await dextools_instance.get_pair(chain, pair)

    assert isinstance(response, dict)
    assert response["statusCode"] == 200
    assert response["data"]["chain"] == chain
    assert response["data"]["address"] == pair

@pytest.mark.asyncio
async def test_get_token_success(dextools_instance):
    chain = "ether"
    token = "0x97a627177634d839968ca935a79bed1e2c9c06f9"
    response = await dextools_instance.get_token(chain, token)

    assert isinstance(response, dict)
    assert response["statusCode"] == 200
    assert response["data"]["chain"] == chain
    assert response["data"]["address"] == token

@pytest.mark.asyncio
async def test_get_chain_list_success(dextools_instance):
    response = await dextools_instance.get_chain_list()
    
    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)

@pytest.mark.asyncio
async def test_get_exchange_list_success(dextools_instance):
    chain = "ether"
    response = await dextools_instance.get_exchange_list(chain)

    assert response["statusCode"] == 200
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)
