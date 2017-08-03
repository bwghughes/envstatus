# project/__init__.py


from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)
app.config.from_object('envstatus.config.DevelopmentConfig')

@app.route('/healthz', methods=['GET'])
def health():
    return jsonify({
        'status': 'success',
    })