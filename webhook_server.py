from flask import Flask, request
import ssl

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    return 'Webhook received'

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('/home/ubuntu/ssl_info/certificate.crt', '/home/ubuntu/ssl_info/private.key')

    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True)
