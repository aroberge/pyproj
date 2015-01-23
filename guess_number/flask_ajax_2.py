'''Simple ajax demo using flask'''

import webbrowser
from flask import Flask, request


def double(n):
    return 2 * n


# ----  flask related stuff follows----------------

app = Flask(__name__, static_folder='')


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/quit')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return '<h3>Server shutting down...</h3>'


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
    webbrowser.open("http://localhost:5000/")  # default for Flask
    app.run()
