from flask import Flask, render_template
import os

app = Flask(__name__, 
           template_folder=os.path.join(os.getcwd(), 'templates'),
           static_folder=os.path.join(os.getcwd(), 'static'))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()