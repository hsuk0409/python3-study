from flask import Flask, g, jsonify, request

app = Flask(__name__)


@app.before_request
def authenticate():
    g.user = 'justin' if not request.authorization else request.authorization['username']


@app.route('/api')
def my_api():
    return jsonify({'username': g.user})


if __name__ == '__main__':
    app.run()
