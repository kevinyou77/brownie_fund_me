from brownie import accounts, network, config, MockV3Aggregator
from dotenv import load_dotenv
from web3 import Web3

FORKED_BLOCKCHAIN_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200_000_000_000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_BLOCKCHAIN_ENVIRONMENTS
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])


def get_address(account):

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]

    if len(MockV3Aggregator) <= 0:
        print(f"Deploying mock aggregator...")

        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})

        print(f"Mock deployed!")

    return MockV3Aggregator[-1].address
