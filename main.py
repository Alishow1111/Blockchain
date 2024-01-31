from blockchain import Blockchain

# Example usage
blockchain = Blockchain()
blockchain.add_new_transaction("Ali pays Tom 1 BTC")
blockchain.mine()
blockchain.add_new_transaction("David pays Zara 0.5 BTC")
blockchain.mine()

# Display the blockchain
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Transactions: {block.transactions}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Current Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}\n")
