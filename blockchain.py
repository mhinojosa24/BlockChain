import hashlib
import time
import json

class BlockChain(object):


    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)


    def proof_of_work(self, last_proof):
        """ This function is where the consensus is implemented """
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1 
            return proof 


    def valid_proof(self, last_proof, proof):
        """ This function validates the proof """
        guess = f'{last_proof}{proof}'.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"


    def new_block(self, proof, previous_hash=None):
        """ This function creates new blocks and adds to the existing chain """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            previous_hash: previous_hash
        }

        # Set the current transaction list to emptpy 
        self.current_transactions = []
        self.chain.append(block)

        return block



    def new_transaction(self, sender, recipient, amount):
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
    def hash(block):
        """ This function creates the hash for a block """

        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        """ This funciton calls and return last block of the chain """

        return self.chain[-1]


    
