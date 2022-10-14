from flask import Flask, redirect
from flaskext.markdown import Markdown
app = Flask(__name__, static_folder='static')
Markdown(app)

from veachron.presentation.ui import blueprint as ui
from veachron.presentation.api import blueprint as api

app.register_blueprint(api)
app.register_blueprint(ui)

@app.route('/')
def hello():
    return redirect('/api/swagger')


def main():
    while True:
        try:
            app.run(host='0.0.0.0', debug=True)
        except SystemExit:
            pass
        except Exception:
            break
