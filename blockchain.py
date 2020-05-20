from block import Block
from datetime import datetime


class BlockChain:
    def __init__(self):
        self.ll = []
        timestamp = str(datetime.now())
        self.ll.append(Block(0, timestamp, "ColdStart", "I am the Genesis Block"))

    def preHash(self):
        return self.ll[len(self.ll)-1].block_hash

    def isvalid(self, newblock):
        cblock = self.ll[-1]
        if newblock.index != cblock.index+1:
            print("index error")
            return False
        elif newblock.previous_hash != cblock.block_hash:
            print("hash error")
            return False
        elif newblock.block_hash != newblock.calc_hash():
            print("hash calc error")
            return False
        else:
            return True

    def addblock(self,data):
        timestamp = str(datetime.now())
        index = len(self.ll)
        previous_hash = self.preHash()
        newblock = Block(index, timestamp, previous_hash, data)

        if self.isvalid(newblock):
            self.ll.append(newblock)
        else:
            print("Invalid da")

    def printchain(self):
        for newblock in self.ll:
            print("Block Index : " + str(newblock.index))
            print("Block Time : " + newblock.timestamp)
            print("Block Previous Hash : " + newblock.previous_hash)
            print("Block Hash : " + newblock.block_hash)
            print("Block Data : " + str(newblock.data))
            print("")







