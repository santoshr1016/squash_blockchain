"""
Resolves ENS domains to Ethereum addresses
ENS is a smart-contract system that registers and resolves `.eth` domains.
"""
import in3


def _print():
    print('\nAddress for {} @ {}: {}'.format(domain, chain, address))
    print('Owner for {} @ {}: {}'.format(domain, chain, owner))


# Find ENS for the desired chain or the address of your own ENS resolver. https://docs.ens.domains/ens-deployments
domain = 'depraz.eth'

print('\nEthereum Name Service')

# Instantiate In3 Client for Goerli
chain = 'goerli'
client = in3.Client(chain, cache_enabled=False)
address = client.ens_address(domain)
owner = client.ens_owner(domain)
_print()

# Instantiate In3 Client for Mainnet
chain = 'mainnet'
client = in3.Client(chain, cache_enabled=False)
address = client.ens_address(domain)
owner = client.ens_owner(domain)
_print()

# Instantiate In3 Client for Kovan
chain = 'kovan'
client = in3.Client(chain, cache_enabled=True)
try:
    address = client.ens_address(domain)
    owner = client.ens_owner(domain)
    _print()
except in3.ClientException:
    print('\nENS is not available on Kovan.')
