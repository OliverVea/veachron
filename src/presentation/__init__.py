from flask import Flask, redirect
from flaskext.markdown import Markdown
app = Flask(__name__, static_folder='static')
Markdown(app)

from presentation.api import blueprint as api
app.register_blueprint(api)

from presentation.ui import blueprint as ui
app.register_blueprint(ui)

from presentation.docs import blueprint as docs
app.register_blueprint(docs)


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
