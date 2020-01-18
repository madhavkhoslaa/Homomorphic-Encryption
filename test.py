from Homomorphic.Encryption import EncryptorBits
from utils.SerDe import SerDe
Serde= SerDe()
A= EncryptorBits()
z= [x for x in range(10)]
encrypted= A.encryptArray(z)
decrypted= A.decryptArray(encrypted)
kk= Serde.Serialise(encrypted)
lol= Serde.Deserialise(kk)
print(lol)