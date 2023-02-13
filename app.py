from flask import Flask
app = Flask(__name__)

if __name__ = '__main__':
    # start Flask test server
    app.run(debug=True, use_reloader=True)