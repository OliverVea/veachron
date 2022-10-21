from flask import Flask, redirect
from flaskext.markdown import Markdown
app = Flask(__name__, static_folder='static')
Markdown(app)

from veachron.presentation.api import blueprint as api

app.register_blueprint(api)

@app.route('/')
def hello():
    return redirect('/api/swagger')


def main():
    app.run(host='0.0.0.0', debug=True, port=5000)
