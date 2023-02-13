import csv
from flask import Flask
from flask import render_template as rt
app = Flask(__name__)

def get_csv():
    csv_path = './static/balt911.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route('/')
def index():
    template = 'index.html'
    object_list = get_csv()
    return rt(template, object_list=object_list)

if __name__ == '__main__':
    # start Flask test server
    app.run(debug=True, use_reloader=True)