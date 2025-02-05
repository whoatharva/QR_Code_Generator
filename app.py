from flask import Flask, send_file, request, render_template
import segno
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr')
def generate_qr():
    text = request.args.get('text', '')
    if text:
        qrcode = segno.make_qr(text)
        img_buffer = io.BytesIO()
        qrcode.save(img_buffer, kind='png', scale=6, border=2)
        img_buffer.seek(0)
        return send_file(img_buffer, mimetype='image/png')
    return 'No text provided', 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)