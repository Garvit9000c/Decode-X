from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import Summary as sp

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
    return "<xmp>" + sp.generate_summary(name,5) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)
