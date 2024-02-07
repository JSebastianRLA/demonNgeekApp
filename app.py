from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Obtiene la dirección IP del cliente desde la solicitud
    ip_address = request.remote_addr
    
    # Renderiza la plantilla HTML y pasa la dirección IP como variable
    return render_template('index.html', ip_address=ip_address)

if __name__ == '__main__':
    app.run(debug=True)
