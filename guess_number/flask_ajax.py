'''Simple ajax demo using flask'''

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return html_content  # see below


@app.route('/_double')
def double_number():
    return str(request.args.get('number', 0, type=int)*2)


# For simplicity, we'll use jQuery
html_content = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script type=text/javascript>
      $(function() {
        $('#calculate').bind('click', function() {
            $.ajax({url:'/_double',
                      data:"number="+$('input[name="a"]').val()
                   }).done(
                        function(data) { $("#result").text(data);
                         });
          return false;
        });
      });
    </script>
  </head>
  <body>
    <h1>Double a number using ajax</h1>

    <form>
      <input type="text" size="5" name="a">
      <button id="calculate">Calculate double:</button>
      <span id="result">?</span>
    </form>

  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
