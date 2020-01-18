import pickle


class SerDe():
    def __init__(self):
        pass

    def Serialise(self, object):
        picklefile = open('dumpdata', 'rb')
        pickle.dump(object, picklefile)




    def Deserialise(self, bits):
        pass
