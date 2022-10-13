from flask import Blueprint, render_template

blueprint = Blueprint('docs', __name__, url_prefix='/docs', template_folder='docs')

@blueprint.route('<path:doc>')
def get_documentation(doc: str):
    return render_template(doc)