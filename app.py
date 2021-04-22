from flask import Flask,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from Summary import *
from convert import *

#Doc
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
                flag=request.form.get('lang')
                if not(request.form.get('mode')):
                        text = request.form['search']
                        if flag:
                                text=English(text)
                        text=Simplifier(text)
                else:
                        file_=request.files['img']
                        filename = secure_filename(file_.filename)
                        s=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        file_.save(s)
                        text=Text_convertor(s,flag)
                        text=Simplifier(text)
                        if flag:
                                text=English(text)
                if request.form.get('type'):
                    return redirect(url_for('legal', name=text))
                else:
                    return redirect(url_for('summary', name=text))


@app.route('/summary/<name>')
def summary(name):
    summary = Format(generate_summary(name))
    # dynamic HTML document
    html = """
    <html>
        <head>
            <!--Meta Declaration-->
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
            <!--Google Fonts-->
            <link href="https://fonts.googleapis.com/css2?family=Averia+Serif+Libre&family=Balsamiq+Sans:wght@700&family=Josefin+Sans:wght@700&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Chelsea+Market&display=swap" rel="stylesheet">
        
            <!--Bootstrap CDN-->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
        
            <!-- Font Awesome CDN -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css"
            integrity="sha256-h20CPZ0QyXlBuAw7A+KluUYx/3pK+c7lYEpqLTlxjYQ="
            crossorigin="anonymous" />
            
            <link rel="stylesheet" href="static/summaryStyle.css">
            <link rel="stylesheet" href="static/header.css">
            
        
            <title>Result | DECODE-X</title>
        </head>
        <body>
            <header>
                <h1>DECODE-X</h1>
                <div class="navBtn">
                  <a href="/">Home</a>
                </div>
            </header>
        
            <h1>Summarised Text</h1>
            <p>{summary}</p>
            
            <h1>Original Text</h1>
            <p>{name}</p>
        </body>
    </html>""".format(summary=summary,name=name)

    return html

@app.route('/legal/<name>')
def legal(name):
    summary= generate_summary(name)
    legal= generate_legal(summary)
    per=(len(legal)/len(summary))*100
    summary=Format(summary)
    legal=Format(legal)
    # dynamic HTML document
    html = """<html>
    <head>
        <title>Result | DECODE-X</title>
    </head>
    <body>
        <a href="/">Home</a>
    
        <h1>Legal</h1>
        <p>{legal}</p>
        
        <h1>Percentage Risk</h1>
        <p>{per}</p>
        
        <h1>Summarised Text</h1>
        <p>{summary}</p>
        
        <h1>Original Text</h1>
        <p>{name}</p>
        
    </body>
    </html>""".format(legal=legal, summary=summary, name=name, per=per)

    return html

if __name__ == '__main__' :
        app.run(debug=True)
