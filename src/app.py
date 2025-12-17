from flask import Flask, request, jsonify
from src.calculator import add, subtract, divide

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    op = data.get('operation')
    a = data.get('a')
    b = data.get('b')
    
    result = 0
    
    try:
        if op == 'add':
            result = add(a, b)
        elif op == 'subtract':
            result = subtract(a, b)
        elif op == 'divide':
            result = divide(a, b)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
            
        return jsonify({'result': result})
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    #para que Docker exponga el endpoint
    app.run(host='0.0.0.0', port=5000)