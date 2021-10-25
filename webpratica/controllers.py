from flask import Blueprint, render_template

webpratica_bp = Blueprint(
    "website",
    __name__,
    template_folder='templates'
)


@webpratica_bp.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@webpratica_bp.route('/contato')
def contato():
    return render_template("contato.html")
