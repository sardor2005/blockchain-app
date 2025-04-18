from flask import Flask, render_template
import os
import hashlib
import time

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
            static_folder=os.path.join(os.path.dirname(__file__), '../static'))

# Ваш блокчейн-код
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

blockchain = []
genesis_block = Block(0, "0", time.time(), "Genesis Block", hashlib.sha256("0".encode()).hexdigest())
blockchain.append(genesis_block.__dict__)

@app.route('/')
def home():
    return render_template('index.html')

# Добавьте остальные ваши роуты (/register, /login и т.д.)

if __name__ == '__main__':
    app.run()
