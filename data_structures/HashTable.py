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


# Test cases
if __name__ == "__main__":

    # Setup
    hash_table = HashTable()

    # Test calculate_hash_value
    print(hash_table.calculate_hash_value('UDACITY'))   # Should be 8568

    # Test lookup edge case
    print(hash_table.lookup('UDACITY'))                 # Should be -1

    # Test store
    hash_table.store('UDACITY')
    print(hash_table.lookup('UDACITY'))                 # Should be 8568

    # Test store edge case
    hash_table.store('UDACIOUS')
    print(hash_table.lookup('UDACIOUS'))                # Should be 8568