import hashlib
import time
import json

class BlockChain(object):


    def __init__(self):
        self.chain = []
        self.current_transactions = []


    def new_block(self, proof, previous_hash=None):
        """ This function creates new blocks and adds to the existing chain """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            previous_hash: previous_hash
        }

        # Set the current transaction list to emptpy 
        self.current_transactions = []
        self.chain.append(block)

        return block



    def new_transaction(self):
        """ This funciton adds a new transaction to already existing transactions """
        
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )

        return self.last_block['index'] + 1


    @staticmethod
    def hash(self, block):
        """ This function creates the hash for a block """

        block_string = json.dumps(block, sort_keys=True).encode()

        reutnr hashlib.sha256(block_string).dexdigest()


    @property
    def last_block(self):
        """ This funciton calls and return last block of the chain """

        return self.chain[-1]


    