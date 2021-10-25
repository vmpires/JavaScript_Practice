from flask import Flask
from webpratica.controllers import webpratica_bp

app = Flask("teste")

app.register_blueprint(webpratica_bp)


if __name__ == "__main__":
    app.run(debug=True)