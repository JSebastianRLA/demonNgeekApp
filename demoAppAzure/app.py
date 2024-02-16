from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
  
    # Obtiene la dirección IP del cliente desde la solicitud
    ip_address = request.remote_addr
    
    # Obtiene el nombre del host del servidor
    hostname = socket.gethostname()
    
    # Renderiza la plantilla HTML y pasa la dirección IP como variable
    return render_template('index.html', ip_address=ip_address, hostname=hostname)

if __name__ == '__main__':
      # app.run(host='127.0.0.1', port=5000)
    app.run(host='192.168.0.168', port=5000)
