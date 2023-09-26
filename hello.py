from flask import Flask, render_template
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)
