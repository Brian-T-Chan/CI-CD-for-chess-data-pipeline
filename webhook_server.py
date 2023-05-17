from flask import Flask, request
import subprocess
import ssl

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():

    if request.method == 'POST':
        subprocess.call(['/home/ubuntu/chess_data/CI-CD-for-chess-data-pipeline/update_repo.sh'])

    return 'Webhook received'

if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('/home/ubuntu/ssl_info/certificate.crt', '/home/ubuntu/ssl_info/private.key')

    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True)

