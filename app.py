from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Obtiene la dirección IP del cliente desde la solicitud
    ip_address = request.remote_addr
    
    # Renderiza la plantilla HTML y pasa la dirección IP como variable
    return render_template('index.html', ip_address=ip_address)
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5000)
    # app.run(host='192.168.0.168', port=5000)
