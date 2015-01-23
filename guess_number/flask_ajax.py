'''Simple ajax demo using flask'''

from flask import Flask, request


def double(n):
    return 2 * n

with open("index.html", 'r') as f:
    html_content = f.read()

# ----  flask related stuff follows----------------

app = Flask(__name__)


@app.route('/')
def index():
    '''Returned by default at the start of the program'''
    return html_content


@app.route('/ajax_double')
def double_number():
    '''retrieves result of ajax query and perform custom function

       The url returned will be of the form:
           /ajax_double?number=X
       where X is the number we wish to double
    '''
    number = request.args.get('number', 0, type=int)
    result = double(number)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
