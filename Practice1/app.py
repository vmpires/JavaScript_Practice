from flask import Flask, render_template

app = Flask("teste")

@app.route('/', methods=['GET'])
def home():
    return (render_template("index.html"))

@app.route('/ola')
def ola():
    return("<h1>Olá mundo do Flask!</h1>")

if __name__ == "__main__":
    app.run(debug=True)