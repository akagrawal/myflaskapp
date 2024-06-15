import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

# Netlify Functions Handler
def handler(event, context):
    from flask import Flask
    from werkzeug.middleware.proxy_fix import ProxyFix
    from werkzeug.serving import run_simple

    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    return run_simple('localhost', 5000, app)

if __name__ == "__main__":
    app.run(debug=True)
