from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    withdraw_weth()


def withdraw_weth():
    """
    Reclaims deposited ETH.
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    withdraw_amount = weth.balanceOf(account, {"from": account})
    print(f"You have {withdraw_amount} WETH")
    tx = weth.withdraw(withdraw_amount, {"from": account})
    tx.wait(1)
    print(f"Recieved {withdraw_amount} WETH")
    return tx
