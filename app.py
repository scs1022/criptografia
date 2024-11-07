from flask import Flask, render_template, request

app = Flask(__name__)

def encriptar_cesar(texto, n):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzñ'
    resultado = ''
    for char in texto.lower():
        if char in alfabeto:
            nuevo_indice = (alfabeto.index(char) + n) % 27
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    return resultado

def desencriptar_cesar(texto, n):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzñ'
    resultado = ''
    for char in texto.lower():
        if char in alfabeto:
            nuevo_indice = (alfabeto.index(char) - n) % 27
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    return resultado

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        texto = request.form.get("texto")
        n = request.form.get("corrimiento")
        accion = request.form.get("accion")

        if texto and n.isdigit():
            n = int(n)
            if accion == "encriptar":
                resultado = encriptar_cesar(texto, n)
            elif accion == "desencriptar":
                resultado = desencriptar_cesar(texto, n)
        else:
            resultado = "Por favor ingrese un texto válido y un número de corrimiento."

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
