import in3


client = in3.Client('goerli')
domain_name = client.ens_namehash('depraz.eth')
# 0x6C095A05764A23156eFD9D603eaDa144a9B1AF33
ens_registry_addr = '0x00000000000c2e074ec69a0dfb2997ba6c7d2e1e'
ens_resolver_abi = 'resolver(bytes32):address'

# Find resolver contract for ens name
resolver_tx = {
    "to": ens_registry_addr,
    "data": client.eth.contract.encode(ens_resolver_abi, domain_name)
}
tx = in3.eth.NewTransaction(**resolver_tx)
encoded_resolver_addr = client.eth.contract.call(tx)
resolver_address = client.eth.contract.decode(ens_resolver_abi, encoded_resolver_addr)

# Resolve name
ens_addr_abi = 'addr(bytes32):address'
name_tx = {
    "to": resolver_address,
    "data": client.eth.contract.encode(ens_addr_abi, domain_name)
}
encoded_domain_address = client.eth.contract.call(in3.eth.NewTransaction(**name_tx))
domain_address = client.eth.contract.decode(ens_addr_abi, encoded_domain_address)

print('END domain:\n{}\nResolved by:\n{}\nTo address:\n{}'.format(domain_name, resolver_address, domain_address))
