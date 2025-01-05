from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dicionário para armazenar a contagem de valores recebidos
value_counts = {}

# Rota principal que renderiza o frontend
@app.route('/')
def index():
    return render_template('index.html')

# Rota que recebe o valor do frontend e retorna a contagem
@app.route('/submit', methods=['POST'])
def submit():
    value = request.form['value']
    
    # Atualiza a contagem do valor recebido
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

    count = value_counts[value]

    if (count > 1):
        return jsonify({"message": f"O valor '{value}' foi recebido {count} vezes."})
    else:
        return jsonify({"message": f"O valor '{value}' foi recebido {count} vez."})

if __name__ == '__main__':
    app.run(debug=True)
