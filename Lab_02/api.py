from flask import Flask, request, jsonify
from Cipher.Caesar import CaesarCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route('/api/Caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/Caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)