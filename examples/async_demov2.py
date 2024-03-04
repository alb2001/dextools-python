import asyncio
from dextools_python import AsyncDextoolsAPIV2
import pprint

pp = pprint.PrettyPrinter(indent=4)

api_key = "YOUR_API_KEY"

# Using an instance, and then closing the connection explicitly at the end:
print("Using an instance, and then closing the connection explicitly at the end:")
async def instance():
    # Initiate DextoolsAPI instance object by passing your "API Key":
    dextools = AsyncDextoolsAPIV2(api_key)

    # Setting your plan after creating the object
    dextools.set_plan("partner")

    # Blockchain
    # Get blockchain info
    print("Get blockchain info")
    blockchain = await dextools.get_blockchain("ether")
    pp.pprint(blockchain)

    # Get blockchains sorted by default settings
    print("Get blockchains sorted by default settings")
    blockchains = await dextools.get_blockchains()
    pp.pprint(blockchains)

    # Get blockchains sorted by default settings and descending order
    print("Get blockchains sorted default settings and descending order")
    blockchains = await dextools.get_blockchains(sort="name", order="desc")
    pp.pprint(blockchains)

    # Exchange
    # Get dex factory info
    print("Get dex factory info")
    factory = await dextools.get_dex_factory_info("ether", "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
    pp.pprint(factory)

    # Get dexes on a specific chain
    print("Get dexes on a specific chain")
    dexes = await dextools.get_dexes("ether")
    pp.pprint(dexes)

    # Get dexes on a specific chain sorted by name and descending order
    print("Get dexes on a specific chain sorted by creationBlock and descending order")
    dexes = await dextools.get_dexes("ether", sort="creationBlock", order="desc")
    pp.pprint(dexes)

    # Pool
    # Get pool info
    print("Get pool info")
    pool = await dextools.get_pool("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
    pp.pprint(pool)

    # Get pool liquidity
    print("Get pool liquidity")
    pool_liquidity = await dextools.get_pool_liquidity("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
    pp.pprint(pool_liquidity)

    # Get pool score
    print("Get pool score")
    pool_score = await dextools.get_pool_score("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
    pp.pprint(pool_score)

    # Get pool price
    print("Get pool price")
    pool_price = await dextools.get_pool_price("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
    pp.pprint(pool_price)

    # Get pools
    print("Get pools")
    pools = await dextools.get_pools("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
    pp.pprint(pools)

    # Get pools sorted by creationBlock and descending order and providing block numbers instead
    print("Get pools sorted by creationBlock and descending order and providing block numbers instead")
    pools = await dextools.get_pools("ether", from_="12755070", to="12755071", sort="creationBlock", order="desc")
    pp.pprint(pools)

    # Token
    # Get token
    print("Get token")
    token = await dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
    pp.pprint(token)

    # Get token locks
    print("Get token locks")
    token_locks = await dextools.get_token_locks("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
    pp.pprint(token_locks)

    # Get token score
    print("Get token score")
    token_score = await dextools.get_token_score("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
    pp.pprint(token_score)

    # Get token info
    print("Get token info")
    token_info = await dextools.get_token_info("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
    pp.pprint(token_info)

    # Get token price
    print("Get token price")
    token_price = await dextools.get_token_price("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
    pp.pprint(token_price)

    # Get tokens
    print("Get tokens")
    tokens = await dextools.get_tokens("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
    pp.pprint(tokens)

    # Get tokens sorted by creationBlock and descending order and providing block numbers instead in descending order
    print("Get tokens sorted by creationBlock and descending order and providing block numbers instead in descending order")
    tokens = await dextools.get_tokens("ether", from_="18570000", to="18570500", sort="creationBlock", order="desc")
    pp.pprint(tokens)

    # Get tokens sorted by socialsInfoUpdated and descending order and datetimes in descending order
    print("Get tokens sorted by socialsInfoUpdated and descending order and providing block numbers instead in descending order")
    tokens = await dextools.get_tokens("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00", sort="socialsInfoUpdated", order="desc")
    pp.pprint(tokens)

    # Get token pools
    print("Get token pools")
    token_pools = await dextools.get_token_pools("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
    pp.pprint(token_pools)

    # Get token pools sorted by creationBlock and descending order and providing block numbers instead in descending order
    print("Get token pools sorted by creationBlock and descending order and providing block numbers instead in descending order")
    token_pools = await dextools.get_token_pools("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", from_="18570000", to="18570500", sort="creationBlock", order="desc")
    pp.pprint(token_pools)

    # Rankings
    # Get hot pools
    print("Get hot pools")
    hot_pools = await dextools.get_ranking_hotpools("ether")
    pp.pprint(hot_pools)

    # Get gainers
    print("Get gainers")
    gainers = await dextools.get_ranking_gainers("ether")
    pp.pprint(gainers)

    # Get losers
    print("Get losers")
    losers = await dextools.get_ranking_losers("ether")
    pp.pprint(losers)

    # Don't forget to close the session
    await dextools.close()

asyncio.run(instance())

print("------------------------------------------------------------------------------------------------------------------")

# Using a context manager, session closing is handled after the context manager ends:
print("Using a context manager, session closing is handled after the context manager ends:")

async def context_manager():
    async with AsyncDextoolsAPIV2(api_key) as dextools:
        # Setting your plan after creating the object
        dextools.set_plan("partner")

        # Blockchain
        # Get blockchain info
        print("Get blockchain info")
        blockchain = await dextools.get_blockchain("ether")
        pp.pprint(blockchain)

        # Get blockchains sorted by default settings
        print("Get blockchains sorted by default settings")
        blockchains = await dextools.get_blockchains()
        pp.pprint(blockchains)

        # Get blockchains sorted by default settings and descending order
        print("Get blockchains sorted default settings and descending order")
        blockchains = await dextools.get_blockchains(sort="name", order="desc")
        pp.pprint(blockchains)

        # Exchange
        # Get dex factory info
        print("Get dex factory info")
        factory = await dextools.get_dex_factory_info("ether", "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
        pp.pprint(factory)

        # Get dexes on a specific chain
        print("Get dexes on a specific chain")
        dexes = await dextools.get_dexes("ether")
        pp.pprint(dexes)

        # Get dexes on a specific chain sorted by name and descending order
        print("Get dexes on a specific chain sorted by creationBlock and descending order")
        dexes = await dextools.get_dexes("ether", sort="creationBlock", order="desc")
        pp.pprint(dexes)

        # Pool
        # Get pool info
        print("Get pool info")
        pool = await dextools.get_pool("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
        pp.pprint(pool)

        # Get pool liquidity
        print("Get pool liquidity")
        pool_liquidity = await dextools.get_pool_liquidity("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
        pp.pprint(pool_liquidity)

        # Get pool score
        print("Get pool score")
        pool_score = await dextools.get_pool_score("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
        pp.pprint(pool_score)

        # Get pool price
        print("Get pool price")
        pool_price = await dextools.get_pool_price("ether", "0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d")
        pp.pprint(pool_price)

        # Get pools
        print("Get pools")
        pools = await dextools.get_pools("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
        pp.pprint(pools)

        # Get pools sorted by creationBlock and descending order and providing block numbers instead
        print("Get pools sorted by creationBlock and descending order and providing block numbers instead")
        pools = await dextools.get_pools("ether", from_="12755070", to="12755071", sort="creationBlock", order="desc")
        pp.pprint(pools)

        # Token
        # Get token
        print("Get token")
        token = await dextools.get_token("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
        pp.pprint(token)

        # Get token locks
        print("Get token locks")
        token_locks = await dextools.get_token_locks("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
        pp.pprint(token_locks)

        # Get token score
        print("Get token score")
        token_score = await dextools.get_token_score("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
        pp.pprint(token_score)

        # Get token info
        print("Get token info")
        token_info = await dextools.get_token_info("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
        pp.pprint(token_info)

        # Get token price
        print("Get token price")
        token_price = await dextools.get_token_price("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a")
        pp.pprint(token_price)

        # Get tokens
        print("Get tokens")
        tokens = await dextools.get_tokens("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
        pp.pprint(tokens)

        # Get tokens sorted by creationBlock and descending order and providing block numbers instead in descending order
        print("Get tokens sorted by creationBlock and descending order and providing block numbers instead in descending order")
        tokens = await dextools.get_tokens("ether", from_="18570000", to="18570500", sort="creationBlock", order="desc")
        pp.pprint(tokens)

        # Get tokens sorted by socialsInfoUpdated and descending order and datetimes in descending order
        print("Get tokens sorted by socialsInfoUpdated and descending order and providing block numbers instead in descending order")
        tokens = await dextools.get_tokens("ether", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00", sort="socialsInfoUpdated", order="desc")
        pp.pprint(tokens)

        # Get token pools
        print("Get token pools")
        token_pools = await dextools.get_token_pools("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", from_="2023-11-14T19:00:00", to="2023-11-14T23:00:00")
        pp.pprint(token_pools)

        # Get token pools sorted by creationBlock and descending order and providing block numbers instead in descending order
        print("Get token pools sorted by creationBlock and descending order and providing block numbers instead in descending order")
        token_pools = await dextools.get_token_pools("ether", "0xfb7b4564402e5500db5bb6d63ae671302777c75a", from_="18570000", to="18570500", sort="creationBlock", order="desc")
        pp.pprint(token_pools)

        # Rankings
        # Get hot pools
        print("Get hot pools")
        hot_pools = await dextools.get_ranking_hotpools("ether")
        pp.pprint(hot_pools)

        # Get gainers
        print("Get gainers")
        gainers = await dextools.get_ranking_gainers("ether")
        pp.pprint(gainers)

        # Get losers
        print("Get losers")
        losers = await dextools.get_ranking_losers("ether")
        pp.pprint(losers)

asyncio.run(context_manager())