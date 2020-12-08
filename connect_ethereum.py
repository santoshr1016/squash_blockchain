import in3


print('\nEthereum Main Network')
client = in3.Client()
latest_block = client.eth.block_number()
gas_price = client.eth.gas_price()
print('Latest BN: {}\nGas Price: {} Wei'.format(latest_block, gas_price))

print('\nEthereum EWC Test Network')
client = in3.Client('ewc')
latest_block = client.eth.block_number()
gas_price = client.eth.gas_price()
print('Latest BN: {}\nGas Price: {} Wei'.format(latest_block, gas_price))

print('\nEthereum Goerli Test Network')
client = in3.Client('goerli')
latest_block = client.eth.block_number()
gas_price = client.eth.gas_price()