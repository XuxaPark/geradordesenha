from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    """Função para gerar uma senha personalizada com os critérios fornecidos."""
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
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

@app.route("/", methods=["GET", "POST"])
def index():
    """Rota principal para exibir a página inicial e processar a geração de senhas."""
    senha_gerada = ""
    tamanho = 12  # Valores padrão
    incluir_maiusculas = True
    incluir_minusculas = True
    incluir_numeros = True
    incluir_simbolos = True

    if request.method == "POST":
        try:
            tamanho = int(request.form.get("tamanho", 12))
        except ValueError:
            tamanho = 12
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
    # Configuração para execução em servidores como Render
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
