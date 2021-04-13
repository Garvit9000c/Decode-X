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
    summary = generate_summary(name,5)
    # dynamic HTML document
    html = """<html>
    <head>
        <title>Result | Nam Abhi pata nahi he</title>
    </head>
    <body>
        <a href="/">Home</a>
    
        <h1>Original Text</h1>
        <p>{name}</p>
        
        <h1>Summarised Text</h1>
        <p>{summary}</p>
    </body>
    </html>""".format(name=name, summary=summary)

    return html


if __name__ == '__main__' :
    app.run(debug=True)
