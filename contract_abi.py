abi = """[
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            }
        ],
        "name": "Change",
        "type": "event"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_newRecipient",
                "type": "address"
            }
        ],
        "name": "approveRecipient",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "id",
                "type": "uint256"
            },
            {
                "name": "max",
                "type": "uint256"
            },
            {
                "name": "price",
                "type": "uint96"
            }
        ],
        "name": "buy",
        "outputs": [],
        "payable": true,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "addr",
                "type": "address"
            }
        ],
        "name": "collectTaxes",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "payable": true,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "forecloseIfPossible",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [],
        "name": "transferRecipient",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "numberOfTokens",
                "type": "uint48"
            },
            {
                "name": "_taxNumerator",
                "type": "uint32"
            },
            {
                "name": "_taxDenominator",
                "type": "uint32"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "name": "accounts",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            },
            {
                "name": "sumOfPrices",
                "type": "uint144"
            },
            {
                "name": "paidThru",
                "type": "uint112"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "newRecipient",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "taxDenominator",
        "outputs": [
            {
                "name": "",
                "type": "uint32"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "addr",
                "type": "address"
            }
        ],
        "name": "taxesDue",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "taxNumerator",
        "outputs": [
            {
                "name": "",
                "type": "uint32"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "taxRecipient",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "tokenCount",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "tokens",
        "outputs": [
            {
                "name": "owner",
                "type": "address"
            },
            {
                "name": "price",
                "type": "uint96"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]"""
