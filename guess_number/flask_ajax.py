'''Simple ajax demo using flask'''

from flask import Flask, request


with open("index.html", 'r') as f:
    html_content = f.read()

app = Flask(__name__)


@app.route('/')
def index():
    return html_content


@app.route('/ajax_double')
def double_number():
    return str(request.args.get('number', 0, type=int)*2)


if __name__ == '__main__':
    app.run(debug=True)
