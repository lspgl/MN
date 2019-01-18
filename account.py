

class Account:
    def __init__(self, addr, key, w3):
        self.addr = addr
        self.key = key
        self.w3 = w3

    @property
    def nonce(self):
        nonce = self.w3.eth.getTransactionCount(self.addr)
        return nonce
