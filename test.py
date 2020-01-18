from Encryption import EncryptorBits

A= EncryptorBits()
z= [x for x in range(10)]
encrypted= A.encryptArray(z)
decrypted= A.decryptArray(encrypted)
print(decrypted== z)