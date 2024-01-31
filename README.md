# Simple Python Blockchain

A basic implementation of a blockchain in Python. This project demonstrates the core concepts of blockchain technology, including creating blocks, adding transactions, and the proof of work mechanism used for mining new blocks.

## Features
- Block creation with timestamp, transaction data, and hashing.
- A proof of work algorithm to secure block creation.
- Mining new blocks with simple transaction data.

## Getting Started

Ensure you have Python 3.6 or above installed on your system. You can verify your Python version by running:

```
python --version
```

## Installation

No external libraries are required for this basic implementation. Clone the repository or download the source code to get started.

## Running the Blockchain

Navigate to the directory containing the blockchain code and run the Python script using:

```
python main.py
```
## How it works

1. **Block Creation**: Each block contains an index, a list of transactions, a timestamp, the hash of the previous block, and a nonce.
2. **Proof of Work**: Blocks are mined through a proof of work process, where the goal is to find a nonce that produces a hash with a certain number of leading zeroes.
3. **Mining**: To mine a new block, transactions are added to the block, and the proof of work process is initiated. Successful mining adds the block to the blockchain.

## Example Usage

After running the script, the blockchain will automatically mine two blocks with example transactions:

- Ali pays Tom 1 BTC
- David pays Zara 0.5 BTC

The output will display the details of each block in the blockchain.

## Customization

You can adjust the difficulty variable in the Blockchain class to make the proof of work mechanism more or less challenging.

## Contributing

Feel free to fork the project, submit pull requests, or send suggestions to improve the code.


