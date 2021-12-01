from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "MINHA-CHAVE-SECRETA"

@app.route('/', methods=["GET"])
def main():
    return render_template('index.html')

@app.route('/sair', methods=["GET"])
def sair():
    session.clear()
    return redirect('/clubetorcedor')

@app.route('/clubetorcedor', methods=['GET','POST'])
def torcedor():
    erros = []

    if request.method == "POST":
        form = request.form
        usuario = form.get('usuario')
        senha = form.get('senha')

        if usuario == "Victor" and senha == "12345":
            session['usuario'] = 'Victor'
            return redirect('/clubetorcedor')
        else:
            erros.append('Usuário e/ou senha incorretos!')    
    
    return render_template(
        'logintorcedor.html',
        erros = erros
    )

if __name__ == "__main__":
    app.run(debug=True)