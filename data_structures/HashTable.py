class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash = self.calculate_hash_value(string)
        if self.table[hash] is None:
            self.table[hash] = [string]
        else:
            self.table[hash].append(string)

    def lookup(self, string):
        hash = self.calculate_hash_value(string)
        if self.table[hash] != None:
            if string in self.table[hash]:
                return hash
        return -1

    def calculate_hash_value(self, string):
        return ord(string[0])*100 + ord(string[1]) 
