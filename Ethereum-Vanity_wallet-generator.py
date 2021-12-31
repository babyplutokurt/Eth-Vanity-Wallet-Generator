# pip install ecdsa
# pip install pysha3

from ecdsa import SigningKey, SECP256k1
import sha3


def checksum_encode(addr_str):  # Takes a hex (string) address as input
    keccak = sha3.keccak_256()
    out = ''
    addr = addr_str.lower().replace('0x', '')
    keccak.update(addr.encode('ascii'))
    hash_addr = keccak.hexdigest()
    for i, c in enumerate(addr):
        if int(hash_addr[i], 16) >= 8:
            out += c.upper()
        else:
            out += c
    return '0x' + out


def test(addrstr):
    assert(addrstr == checksum_encode(addrstr))


X = 0
address = "00000000000000000000000000000000"
Vanity = '55555'
Vanity_length = len(Vanity)
while address[0:0+Vanity_length] != Vanity:

    keccak = sha3.keccak_256()
    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()
    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    X = X+1
    print(X)
"""if you wang to produce a ether wallet like 0x00000, set Vanity=00000"""


print("Private key:", priv.to_string().hex())
print("Public key: ", pub.hex())
print("Address:    ", checksum_encode(address))
