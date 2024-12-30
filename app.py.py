from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    if not caracteres:
        return "Selecione pelo menos uma opção!"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = ""
    # Valores padrão
    tamanho = 12
    incluir_maiusculas = True
    incluir_minusculas = True
    incluir_numeros = True
    incluir_simbolos = True

    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 12))
        incluir_maiusculas = "maiusculas" in request.form
        incluir_minusculas = "minusculas" in request.form
        incluir_numeros = "numeros" in request.form
        incluir_simbolos = "simbolos" in request.form
        senha_gerada = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)

    return render_template("index.html", senha=senha_gerada, tamanho=tamanho,
                           incluir_maiusculas=incluir_maiusculas,
                           incluir_minusculas=incluir_minusculas,
                           incluir_numeros=incluir_numeros,
                           incluir_simbolos=incluir_simbolos)

if __name__ == "__main__":
    app.run(debug=True)
