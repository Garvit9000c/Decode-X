from flask import Flask, render_template, request, redirect, url_for
from Summary import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    name=generate_summary(name,5)
    # dynamic HTML document
    html = """<html>
    <head></head>
    <body><h1>{name}</h1></body>
    </html>""".format(name=name)

    return html


if __name__ == '__main__' :
    app.run(debug=True)
