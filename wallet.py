# Import dependencies
import subprocess
import json
from dotenv import load_dotenv


# Load and set environment variables
load_dotenv()
# mnemonic=os.getenv("mnemonic")
mnemonic = "capital sleep habit gas power license slight fruit garden quiz surge access"
# Import constants.py and necessary functions from bit and web3
from constants import *
import os
from web3 import Web3
from dotenv import load_dotenv

 

# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = f'./derive --mnemonic="{mnemonic}" --coin={coin} --numderive={numderive} --format=json -g'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)
    
# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = "ETH"
all_coins = [
    ETH: derive_wallets(mnemonic, ETH, 3),
    BTCTEST: derive_wallets(mnemonic, BTCTEST, 3)
]

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
def priv_key_to_account(priv_key):
    return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(account, to, amount):
    return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, "btc")])
    
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.   
def send_tx(account, to, amount):
    raw_tx = create_tx(account, to, amount)
    signed = account.sign_transaction(raw_tx)
    return NetworkAPI.broadcast_tx_testnet(signed)
account = priv_key_to_account("Placeholder for private key")
send_tx(account, "Placeholder for recipient address", 0.0001)