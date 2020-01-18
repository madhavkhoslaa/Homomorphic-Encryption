import pickle
import base64
import pickle 
import os


class SerDe():
    def __init__(self):
        pass

    def Serialise(self, object, key):
        """Returns the binary data into a base 64 encoded values"""
        payload = {}
        picklefile = open('datadump', 'wb')
        pickle.dump(object, picklefile)
        picklefile.close()
        f=open("datadump", "rb")
        payload['content'] = base64.b64encode(f.read())
        os.system("rm -rf datadump")
        payload["public key"]= key
        return payload

    def Deserialise(self, payload):
        """Expects a dictionary of base54 encoded binary values of a 
        Serialised object"""
        #Decoding the base64 values
        fileData = base64.b64decode(payload['content'])
        #Creating a byte array to write the file
        newFileByteArray = bytearray(fileData)
        f= open("datadump","w+b")
        f.write(newFileByteArray)
        picklefile = open("datadump", "rb")
        object = pickle.load(picklefile, encoding="bytes")
        picklefile.close()
        os.system("rm -rf datadump")
        return object