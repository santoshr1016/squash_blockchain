import in3

print('\nEthereum Goerli Test Network')
client = in3.Client('goerli')
node_list = client.refresh_node_list()
print('\nIncubed Registry:')
print('\ttotal servers:', node_list.totalServers)
print('\tlast updated in block:', node_list.lastBlockNumber)
print('\tregistry ID:', node_list.registryId)
print('\tcontract address:', node_list.contract)
print('\nNodes Registered:\n')
for node in node_list.nodes:
    print('\turl:', node.url)
    print('\tdeposit:', node.deposit)
    print('\tweight:', node.weight)
    print('\tregistered in block:', node.registerTime)
    print('\n')