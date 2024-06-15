from flask import Flask, request, render_template
import pyotp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    secret = request.form['secret']
    totp = pyotp.TOTP(secret)
    code = totp.now()
    return render_template('index.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)
