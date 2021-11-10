from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('Birthday.html')


@app.route('/gift.html')
def gift():
    return render_template('gift.html')


@app.route('/secret.html')
def secret():
    return render_template('secret.html')




