from flask import Flask
from flask import render_template as rt
app = Flask(__name__)

@app.route('/')
def index():
    template = 'index.html'
    return rt(template)

if __name__ == '__main__':
    # start Flask test server
    app.run(debug=True, use_reloader=True)