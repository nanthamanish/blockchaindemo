import hashlib


class Block:

    def calc_hash(self):
        string_to_hash = str(self.index) + str(self.timestamp) + self.previous_hash + str(self.data)
        return hashlib.sha256(string_to_hash.encode()).hexdigest()

    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.block_hash = self.calc_hash()