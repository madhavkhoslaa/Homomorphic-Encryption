from phe import paillier


class EncryptorBits():
    def __init__(self):
        self.public_key, self.private_key = paillier.generate_paillier_keypair()


    def encryptArray(self, data): 
        encrypted_number_list = [self.public_key.encrypt(x) for x in data]
        return encrypted_number_list

    
    def decryptArray(self, edata):
        decrypted_number_list= [self.private_key.decrypt(x) for x in edata]
        return decrypted_number_list