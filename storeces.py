#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from web3 import Web3
import json
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.eth.default_account = w3.eth.accounts[0] 
with open("CESRegistry_abi.json") as f:
    abi = json.load(f)
contract_address = "0xYourDeployedContractAddress"
ces_contract = w3.eth.contract(address=contract_address, abi=abi)
tx_hash = ces_contract.functions.storeCES(
    fingerprint,
    signature.hex()
).transact()
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction successful:", receipt.transactionHash.hex())


# In[ ]:


#store json file
import json
output = {
    "fingerprint": fingerprint,
    "signature": signature.hex(),
    "valid": is_valid
}
with open("ces_metadata.json", "w") as f:
    json.dump(output, f, indent=4)


# In[ ]:




