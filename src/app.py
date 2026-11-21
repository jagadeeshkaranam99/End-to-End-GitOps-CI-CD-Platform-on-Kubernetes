from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/info', methods=['GET'])
def get_info():
    return jsonify({
        "name": "python-app",
        "version": "1.0.0",
        "description": "Containerized Python Flask REST API for End-to-End GitOps CI/CD Platform"
    }), 200

@app.route('/api/v1/healthz', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
