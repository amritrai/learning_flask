from flask import Flask

app: Flask = Flask(__name__)


# @signifies a decorator - way to wrap a function and modifying its behaviour.
@app.route('/')
def index():
    return 'This is the homepage.'


@app.route('/tuna')
def tuna():
    return '<h1> Tuna is good. </h1>'


@app.route('/profile/<string>')
def username(string):
    return "Hey there %s" % string

@app.route('/post/<int:post_id>')
def designation(post_id):
    return "Your post ID is: %i" % post_id

if __name__ == "__main__":
    app.run(debug=True)


