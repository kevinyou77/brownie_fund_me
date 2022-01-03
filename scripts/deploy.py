from brownie import FundMe, config, network
from scripts.helper import get_account, get_address
from dotenv import load_dotenv

load_dotenv()


def deploy_fund_me():
    account = get_account()

    print(f"The active network is {network.show_active()}")
    print(f"Deploying...")

    fund_me = FundMe.deploy(
        get_address(account),
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    print(f"Deployed!")

    return fund_me


def main():
    deploy_fund_me()
