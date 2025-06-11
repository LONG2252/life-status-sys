from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    if 'value' in data:
        return jsonify({'value': data['value']})
    else:
        return jsonify({'error': 'Missing value parameter'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
