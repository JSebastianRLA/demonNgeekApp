from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
  
    # Obtiene la dirección IP del cliente desde la solicitud
    ip_address = request.remote_addr
    
    # Obtiene el nombre del host del servidor
    # Intenta resolver inversamente la dirección IP para obtener el nombre de host
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        hostname = "No se pudo obtener el nombre de host"
    # Obtener headers
    
    headerssss = request.headers
    
    # Renderiza la plantilla HTML y pasa la dirección IP como variable
    return render_template('index.html', ip_address=ip_address, hostname=hostname, headerssss=headerssss)

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5000)
    # app.run(host='192.168.0.168', port=5000)
