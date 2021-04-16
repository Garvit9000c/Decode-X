from flask import Flask,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from Summary import *
from convert import *


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
        if request.method == 'POST':
                if not(request.form.get('mode')):
                        text = English(Simplifier(request.form['search']))
                else:
                        file_=request.files['img']
                        filename = secure_filename(file_.filename)
                        s=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        file_.save(s)
                        text=English(Simplifier(Text_convertor(s)))
                        
                if request.form.get('type'):
                    return redirect(url_for('legal', name=text))
                else:
                    return redirect(url_for('summary', name=text))


@app.route('/summary/<name>')
def summary(name):
    summary = generate_summary(name,5)
    # dynamic HTML document
    html = """<html>
    <head>
        <title>Result | DECODE-X</title>
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
    
@app.route('/legal/<name>')
def legal(name):
    summary = name
    # dynamic HTML document
    html = """<html>
    <head>
        <title>Result | DECODE-X</title>
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
