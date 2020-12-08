import in3

in3_client = in3.Client()
# Sends a request to the Incubed Network, that in turn will collect proofs from the Ethereum client,
# attest and sign the response, then send back to the client, that will verify signatures and proofs.
block_number = in3_client.eth.block_number()
print(block_number) # Mainnet's block number

print(in3_client)  # incubed network api
print(in3_client.eth)  # ethereum api
# print(in3_client.account)  # ethereum account api
# print(in3_client.contract)  # ethereum smart-contract api