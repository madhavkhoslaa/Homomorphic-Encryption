from Homomorphic.Encryption import EncryptorBits
from utils.SerDe import SerDe
Serde= SerDe()
A= EncryptorBits()
z= [x for x in range(10)]
x= [2*x for x in range(10)]

encrypted= A.encryptArray(z)
encrypted2= A.encryptArray(x)
decrypted= A.decryptArray(encrypted)
kk= Serde.Serialise(encrypted)
lol= Serde.Deserialise(kk)
meme= encrypted+ encrypted2
print(meme)