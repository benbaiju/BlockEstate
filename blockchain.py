import random
import sys
import base64

import json

from web3 import Web3
from solcx import compile_standard

import solcx
# solcx.install_solc()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "phb.sol": {
            "content": '''
                 pragma solidity >=0.4.0 <0.8.21;
               

                contract PHB {

                     struct User
                    {
    
                        int user_id1;
                        string username1;
                        string password1;
                        string mobile1;
                        string p_address1;
                        string uaddress1;
                        string gender1;
                        string name1;
                    }

                    User []uss;

                    function addUser(int user_id1,string memory username1,string memory password1,string memory name1,string memory mobile1,string memory p_address1,string memory uaddress1,string memory gender1) public
                    {
                        User memory e 
                            =User(user_id1,
                                    username1,
                                    password1,
                                    name1,
                                    mobile1,
                                    p_address1,
                                    uaddress1,
                                    gender1);
                        uss.push(e);
                    }


                    function getUser(int user_id1) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<uss.length;i++)
                        {
                            User memory e
                                =uss[i];
                            if(e.user_id1==user_id1)
                            {
                                return(e.username1,
                                    e.password1,
                                    e.mobile1,
                                    e.p_address1,
                                    e.uaddress1,
                                    e.gender1,
                                    e.name1
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }
                    function getUserCount() public view returns(uint256)
                    {
                        return(uss.length);
                    }
                    struct Ptoken
                    {
                        int idd;
                        string ptype;
                        string p_id;
                        string tok_name;
                        string file_name;
                        string amn;
                        string curr;
                        string hs;
                        string username;
                    }
                    Ptoken []tprc;
                    function addtok_prp(int idd,string memory ptype,string memory p_id,string memory tok_name,string memory file_name,string memory amn,string memory curr,string memory hs,string memory username) public
                    {
                        Ptoken memory e
                            =Ptoken(idd,
                                    ptype,
                                    p_id,
                                    tok_name,
                                    file_name,
                                    amn,
                                    curr,
                                    hs,
                                    username);
                        tprc.push(e);
                    }
                    struct Property
                    {
                        int us3;
                        string prid3;
                        string uname3;
                        string ptype3;
                        string details3;
                        string file_name3;
                        string amount3;
                        string status;
                        string phn;
                        string hash1;
                    }

                    Property []prc;
                    function addProp(int us3,string memory prid3,string memory uname3, string memory ptype3,string memory details3, string memory file_name3,string memory amount3,string memory status,string memory phn,string memory hash1) public
                    {
                        Property memory e
                            =Property(us3,
                                    prid3,
                                    uname3,
                                    ptype3,
                                    details3,
                                    file_name3,
                                    amount3,
                                    status,
                                    phn,
                                    hash1);
                        prc.push(e);
                    }
                    function getPrp(int us3) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory)
                    {
                        uint i;
                        for(i=0;i<prc.length;i++)
                        {
                            Property memory e
                                =prc[i];
                            if(e.us3==us3)
                            {
                                return(e.prid3, 
                                    e.uname3,
                                    e.ptype3,
                                    e.details3,
                                    e.file_name3,
                                    e.amount3,
                                    e.status,
                                    e.phn,
                                    e.hash1
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }
                    function getPrpCount() public view returns(uint256)
                    {
                        return(prc.length);
                    }
                    struct Transaction
                    {
                        int t_id4;
                        string name4;
                        string paddr24;
                        string nmr4;
                        string paddr14;
                        string pid4;
                        string amount4;
                        string t_hash4;
                    }
                    Transaction []transactions;

                    function addTransaction(int t_id4,string memory name4,string memory paddr24,string memory nmr4,string memory paddr14,string memory pid4,string memory amount4,string memory t_hash4)public
                    {
                        Transaction memory t=Transaction(t_id4,
                                                        name4,
                                                        paddr24,
                                                        nmr4,
                                                        paddr14,
                                                        pid4,
                                                        amount4,
                                                        t_hash4);
                        transactions.push(t);
                    }

                    function getTransaction(int t_id4) public view returns(string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory)
                    {
                        uint j;
                        for(j=0;j<transactions.length;j++)
                        {
                            Transaction memory t=transactions[j];

                            if(t.t_id4==t_id4)
                            {
                                return(t.name4,
                                        t.paddr24,
                                        t.nmr4,
                                        t.paddr14,
                                        t.pid4,
                                        t.amount4,
                                        t.t_hash4);
                            }

                        }

                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }
                    function getTransactionsCount() public view returns(uint256)
                    {
                        return(transactions.length);
                    }
                    }

               '''
        }
    },
    "settings":
    {
        "outputSelection": {
            "*": {
                "*": [
                    "metadata", "evm.bytecode", "evm.bytecode.sourceMap"
                ]
            }
        }
    }
})


# web3.py instance


def create_contract():
    blockchain_address = 'HTTP://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    # get bytecode
    bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])[
        'output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)

    # # Submit the transaction that deploys the contract
    tx_hash = pb.constructor().transact()

    # # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ", tx_receipt.contractAddress)
    f = open('contract_address.txt', 'w')
    f.write(tx_receipt.contractAddress)
    f.close()
    f1 = open('s_id.txt', 'w')
    f1.write('0')
    f1.close()
    f2 = open('tk_id.txt', 'w')
    f2.write('0')
    f2.close()


def get_user(id1):
    id1 = int(id1)
    p1 = get_contract()
    print(id1, '============')
    store = p1.functions.getUser(id1).call()
    print('store1:', store)
    return store


def get_users():
    c = get_user_count()
    c_names = ['username', 'password', 'name',
               'mobile', 'p_address', 'address', 'gender']
    dict1 = {}
    for i in range(1, c+1):
        d = get_user(i)
        print('d:', d)
        dict2 = {}
        for j in range(len(c_names)):
            print('d:', d[j])
            dict2[c_names[j]] = d[j]
        dict1[i] = dict2

    print(dict1)
    return dict1


def get_user_count():
    p1 = get_contract()
    store = p1.functions.getUserCount().call()
    print('##################################')
    print('store:', store)
    print('##################################')
    return int(store)


def verify_key(adr1, key):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr1,
            'value': web3.toWei(1, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(1, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx, key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        # print(web3.toHex(tx_hash))
        return "Yes"
    except Exception as e:
        print(e)
        return "No"


def add_user1(user_id, username, password, name, mobile, p_address, uaddress, gender):
    f = open('contract_address.txt', 'r')
    address = f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])[
        'output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    tx_hash = p1.functions.addUser(
        user_id, username, password, name, mobile, p_address, uaddress, gender).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)


def add_prop(us, Prop_id, username, ptype, details, file_name, amount, status, phn, hash1):
    print("#######:", us, Prop_id, username, ptype,
          details, file_name, amount, status, phn, hash1)
    f = open('contract_address.txt', 'r')
    address = f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])[
        'output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )

    tx_hash = p1.functions.addProp(
        us, Prop_id, username, ptype, details, file_name, amount, status, phn, hash1).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)


def get_contract():
    f = open('contract_address.txt', 'r')
    address = f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    # '0x3529A6ee990639C32bEe5F841a9649cdd0c6e0FD'
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

    # get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])[
        'output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    print("H#####################################################I")
    print(p1)
    print("H#####################################################I")
    return p1
#######################################################################


def get_prp(id1):
    id1 = int(id1)
    p1 = get_contract()
    print(id1, '============')
    store = p1.functions.getPrp(id1).call()
    print('store1:', store)
    return store


def get_prps():
    c = get_prp_count()
    print("#############c:", c)
    c_names = ['Prop_id', 'username', 'ptype', 'details',
               'file_name', 'amount', 'status', 'phone', 'hash1']
    dict1 = {}
    for i in range(1, c+1):
        d = get_prp(i)
        print('d:', d)
        dict2 = {}
        for j in range(len(c_names)):
            print('d:', d[j])
            dict2[c_names[j]] = d[j]
        dict1[i] = dict2

    print(dict1)
    return dict1


def get_prp_count():
    p1 = get_contract()
    store = p1.functions.getPrpCount().call()
    print('##################################')
    print('store:', store)
    print('##################################')
    return int(store)
################################################################################


def verify_adr(s):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected(), "##########")
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    adrs = w3.eth.accounts
    print(adrs)

    if s in adrs:
        return True
    else:
        return False
#################################################################################


def transfer(adr1, adr2, key, amount):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr2,
            'value': web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(amount, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx, key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
        generated_hash = web3.toHex(tx_hash)
        print("generated_hash : ", generated_hash)
        return generated_hash

    except Exception as e:
        print(e)
        return False
################################################################################


def add_transaction_to_table(get_id, name, paddr2, nmr, paddr1, pid, amount, t_hash):
    f = open('contract_address.txt', 'r')
    address = f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

    # get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])[
        'output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    tx_hash = p1.functions.addTransaction(
        get_id, name, paddr2, nmr, paddr1, pid, amount, t_hash).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    # print(tx_hash)
    print(tx_receipt)


def get_transact(id1):
    id1 = int(id1)
    p1 = get_contract()
    store = p1.functions.getTransaction(id1).call()
    print("store : ", store)
    return store


def get_transactions():
    c = get_transactionss_count()

    c_names = ['Sender_name', 'Sender_address', 'Receiver_name',
               'Receiver_address', 'Prp_id', 'Amount', 'T_hash']
    dict1 = {}
    for i in range(1, c+1):
        d = get_transact(i)
        dict2 = {}
        for j in range(len(c_names)):
            dict2[c_names[j]] = d[j]
        dict1[i] = dict2

    print(dict1)
    return dict1


def get_transactionss_count():
    p1 = get_contract()
    store = p1.functions.getTransactionsCount().call()
    print(store)
    return int(store)
####################################################################################################
    # Token Functions
####################################################################################################


def tkadd(idd, ptype, p_id, tok_name, file_name, amn, cu_owner, hashh, username):
    f = open('contract_address.txt', 'r')
    address = f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    # w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])[
        'output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )

    print("Type of idd::", type(idd))
    idd = int(idd)
    ptype = str(ptype)
    p_id = str(p_id)
    tok_name = str(tok_name)
    file_name = str(file_name)
    amn = str(amn)
    cu_owner = str(cu_owner)
    hashh = str(hashh)
    username = str(username)
    tx_hash = p1.functions.addtok_prp(
        idd, ptype, p_id, tok_name, file_name, amn, cu_owner, hashh, username).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)


####################################################################################################
if __name__ == "__main__":
    # pass
    create_contract()
