from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length].upper()
            shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length].upper()
            shift = ord(key_char) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    plain_text = request.form['plain_text']
    key = request.form['key']
    encrypted_text = encrypt(plain_text, key)
    return render_template('index.html', result=encrypted_text)

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    encrypted_text = request.form['encrypted_text']
    key = request.form['key']
    decrypted_text = decrypt(encrypted_text, key)
    return render_template('index.html', result=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
