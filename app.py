from flask import Flask, render_template, jsonify
from flask_cors import CORS
import random
app = Flask(__name__, template_folder='templates')
CORS(app)
@app.route('/')
def index():
    # Ingu 4 spaces kandaipa irukanum
    return render_template('index.html')

@app.route('/optimize', methods=['GET'])
def optimize():
    # Ingu dictionary-ku munnadi 4 spaces irukanum
    data = {
        "cpu_usage": [random.randint(20, 80) for _ in range(10)],
        "memory_usage": [random.randint(30, 90) for _ in range(10)],
        "status": "Optimizing..."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()

