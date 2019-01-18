from web3 import Web3, HTTPProvider
import contract_abi
from account import Account
from colors import Colors as _C

import time


class HarbergerInterface:
    def __init__(self):
        INFURA_URL = "https://ropsten.infura.io/v3/57432904133046c490a8ff1a850c0ee9"
        self.w3 = Web3(HTTPProvider(INFURA_URL))

        CONTRACT_ADDR = self.w3.toChecksumAddress("0x6790481100a7739b70faa93877a6822e92444e17")

        ROOT_ADDR = "0xf7dCaAc33578B78eF3D40Cbf4886f97F3b3427AB"
        ROOT_PRIVATE_KEY = "B644C06B01FC46203202D311C6014003C0D747FFAB4D5B467BFF81C34E7F839F"
        self.root = Account(ROOT_ADDR, ROOT_PRIVATE_KEY, self.w3)

        DEV_ALPHA_ADDR = "0xFc7404e9F20DC97114350399dFd0a04E47F0bc90"
        DEV_ALPHA_PRIVATE_KEY = "7A4F9E771123A4AC2F0565E72FB3DFA16F0EDF7839261CB90DACD25006C2E050"
        alpha = Account(DEV_ALPHA_ADDR, DEV_ALPHA_PRIVATE_KEY, self.w3)

        DEV_BETA_ADDR = "0x436276Cb21971FB982f66fB2Ce3262ABb40A01d9"
        DEV_BETA_PRIVATE_KEY = "2A2853D5D117082137EAD67AA18AD467F4BC4F36FD38EB4A85B2B3286F226767"
        beta = Account(DEV_BETA_ADDR, DEV_BETA_PRIVATE_KEY, self.w3)

        self.clients = {'alpha': alpha, 'beta': beta}

        self.contract = self.w3.eth.contract(address=CONTRACT_ADDR, abi=contract_abi.abi)

        # self.contractPrint(self.contract)

        # self.w3.eth.enable_unaudited_features()

    def contractPrint(self, contract):
        print('-' * 100)
        print('Contract Address: ' + contract.address)
        print('ABI:')

        for a in contract.abi:
            print('-' * 50)
            if a['type'] == 'function':
                if a['constant']:
                    color = _C.BLUE
                else:
                    color = _C.MAGENTA
                print(color + (' ' + a['name'] + ' ').center(50, '*') + _C.ENDC)
            else:
                print(_C.LIGHT + (' ' + a['type'] + ' ').center(50, '*') + _C.ENDC)
            print('-' * 50)
            for key in a:
                if key not in ['name', 'type', 'constant']:
                    print(_C.YEL + key + _C.ENDC + ': ', end='')
                    if key in ['inputs', 'outputs']:
                        print()
                        values = a[key]
                        if len(values) == 0:
                            print(' ' * 4 + _C.RED + 'None' + _C.ENDC)
                        else:
                            for i in values:
                                print(' ' * 4 + _C.LIME + i['type'] + _C.ENDC + ' :: ' + _C.CYAN + i['name'] + _C.ENDC)
                    else:
                        print(str(a[key]))

    def receiptPrint(self, receipt):
        block = receipt['blockNumber']
        status = receipt['status']
        gasUsed = receipt['gasUsed']
        print('-' * 50)
        print(_C.YEL + 'BLOCK:  ' + _C.ENDC + str(block))
        if status == 1:
            color = _C.LIME
        else:
            color = _C.RED
        print(_C.YEL + 'STATUS: ' + _C.ENDC + color + str(status) + _C.ENDC)
        print(_C.YEL + 'GAS:    ' + _C.ENDC + str(gasUsed))

    def tokenOverview(self):
        nTokens = self.contract.functions.tokenCount().call()
        print(nTokens)
        for n in range(nTokens):
            tkn = self.contract.functions.tokens(n).call()
            print(tkn)

    def accountOverview(self, acc):
        keys = ['balance', 'sumOfPrices', 'paidThru']
        overview = self.contract.functions.accounts(acc.addr).call()
        accOverview = dict(zip(keys, overview))
        print(accOverview)
        return accOverview

    def waitForReciept(self, timeout, result):
        txn_receipt = self.w3.eth.getTransactionReceipt(result)
        t0 = time.time()
        dt = 0
        while txn_receipt is None and (dt < timeout):
            txn_receipt = self.w3.eth.getTransactionReceipt(result)
            dt = time.time() - t0
            print('Timeout in ' + str(round(60 - dt, 1)) + '' * 10, end='\r')

        if txn_receipt is not None:
            print('Reciept after ' + str(round(dt, 1)))
            self.receiptPrint(txn_receipt)
        else:
            print('Timeout after ' + str(timeout) + 's')

        return txn_receipt

    def deposit(self, account, amount):
        print('-' * 100)
        print('Depositing', amount, 'ETH to Nation Account')
        print('Client:', account.addr)
        amount_in_wei = self.w3.toWei(amount, 'ether')
        nonce = account.nonce
        txn_dict = self.contract.functions.deposit().buildTransaction({
            'value': amount_in_wei,
            'chainId': 3,
            'gas': 2000000,
            'gasPrice': self.w3.toWei('40', 'gwei'),
            'nonce': nonce
        })

        signed_txn = self.w3.eth.account.signTransaction(txn_dict, private_key=account.key)
        result = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        txn_receipt = self.waitForReciept(60, result)

        if txn_receipt is None:
            return {'status': 'failed', 'error': 'timeout'}

        return {'status': 'added', 'txn_receipt': txn_receipt}

    def withdraw(self, account, amount):
        print('-' * 100)
        print('Withdrawing', amount, 'ETH from Nation Account')
        print('Client:', account.addr)
        amount_in_wei = self.w3.toWei(amount, 'ether')
        nonce = account.nonce
        txn_dict = self.contract.functions.withdraw(amount_in_wei).buildTransaction({
            'chainId': 3,
            'gas': 2000000,
            'gasPrice': self.w3.toWei('400', 'gwei'),
            'nonce': nonce
        })

        signed_txn = self.w3.eth.account.signTransaction(txn_dict, private_key=account.key)
        result = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        txn_receipt = self.waitForReciept(60, result)

        if txn_receipt is None:
            return {'status': 'failed', 'error': 'timeout'}

        return {'status': 'added', 'txn_receipt': txn_receipt}


if __name__ == '__main__':
    interface = HarbergerInterface()

    alpha = interface.clients['alpha']
    beta = interface.clients['beta']
    interface.accountOverview(alpha)
    # interface.deposit(alpha, 0.5)
    interface.accountOverview(alpha)
    interface.withdraw(alpha, 0.5)
    interface.accountOverview(alpha)
    # interface.tokenOverview()

    # interface.deposit(interface.clients['alpha'], 0.001)
