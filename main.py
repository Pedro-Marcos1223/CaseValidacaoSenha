from flask import Flask, request, jsonify
import re

# Inicializa a aplicação Flask
app = Flask(__name__)

# Função para validar a senha de acordo com os critérios
def validate_password(password):

    """
        Valida uma senha de acordo com os critérios definidos.

        Args:
            password (str): A senha a ser validada.

        Returns:
            bool: True se a senha é válida, False caso contrário.
        """

    if (' ' in password) or (len(password) < 9) or \
            (not re.search(r'\d', password)) or \
            (not re.search(r'[a-z]', password)) or \
            (not re.search(r'[A-Z]', password)) or \
            (not re.search(r'[!@#$%^&*()-+]', password)) or \
            (re.search(r'(.)\1', password)):
        return False
    return True

# Rota que verifica a senha
@app.route('/validate_password', methods=['POST'])
def check_password():

    """
        Rota para verificar a validade de uma senha fornecida por uma requisição POST.

        Returns:
            JSON: Uma resposta JSON indicando se a senha é válida ou não.
        """

    data = request.get_json()
    password = data.get('password')

    # Verifica se a senha foi fornecida
    if password is None:
        return jsonify({"error": "Password not provided"}), 400

    # Verifica se a senha é válida
    if validate_password(password):
        return jsonify({"message": "Password is valid"}), 200
    else:
        return jsonify({"message": "Password is not valid"}), 400

# Inicializa o servidor se este arquivo for executado diretamente
if __name__ == '__main__':
    app.run()