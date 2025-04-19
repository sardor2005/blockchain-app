from flask import Flask, render_template, jsonify
import os
import time
import hashlib

app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')

# Блокчейн
class Block:
    def __init__(self, index, prev_hash, data):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.data = data
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.prev_hash}{self.timestamp}{self.data}".encode()).hexdigest()

blockchain = [Block(0, "0", "Genesis Block")]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/mine', methods=['POST'])
def mine():
    last_block = blockchain[-1]
    new_block = Block(len(blockchain), last_block.hash, f"Block #{len(blockchain)}")
    blockchain.append(new_block)
    return jsonify({
        "message": "New block mined!",
        "index": new_block.index,
        "hash": new_block.hash
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
