import in3
import json

chain = 'mainnet'
client = in3.Client(chain)
domain_name = client.ens_namehash('depraz.eth')
ens_registry_addr = '0x6C095A05764A23156eFD9D603eaDa144a9B1AF33'
ens_resolver_abi = 'resolver(bytes32):address'
tx_data = client.eth.contract.encode(ens_resolver_abi, domain_name)
print(tx_data)
resolver_tx = {
    "to": ens_registry_addr,
    "data": tx_data
}
tx = in3.eth.NewTransaction(**resolver_tx)
print(tx)
encoded_resolver_addr = client.eth.contract.call(tx)
print(encoded_resolver_addr)
# client.eth.contract.decode(ens_resolver_abi, encoded_resolver_addr)



# domain_name = client.ens_namehash('depraz.eth')
# ens_registry_addr = '0x6C095A05764A23156eFD9D603eaDa144a9B1AF33'
# ens_resolver_abi = 'resolver(bytes32):address'


# node_list = client.refresh_node_list()
#
# print('\nIncubed Registry:')
# print('\ttotal servers:', node_list.totalServers)
# print('\tlast updated in block:', node_list.lastBlockNumber)
# print('\tregistry ID:', node_list.registryId)
# print('\tcontract address:', node_list.contract)
# print('\nNodes Registered:\n')
# for node in node_list.nodes:
#     print('\turl:', node.url)
#     print('\tdeposit:', node.deposit)
#     print('\tweight:', node.weight)
#     print('\tregistered in block:', node.registerTime)
#     print('\n')

# 0x6C095A05764A23156eFD9D603eaDa144a9B1AF33