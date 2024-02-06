from flask import Flask, render_template
import requests  # Importa la biblioteca para realizar solicitudes HTTP

app = Flask(__name__)

@app.route('/')
def index():
    # Lista de nombres de imágenes para pasar a la plantilla HTML
    imagenes = [
        'f5-logo.png', 
        'ngeekImagotipo.png',
        'ngeekTipografiWithe.png' ]  # Agrega más imágenes si es necesario
    
    url = 'http://192.168.0.170:30808/'
    response = requests.get(url)
    data = response.json()  # Obtiene los datos de la respuesta en formato JSON
    
    # Pasa los datos a la plantilla HTML
    return render_template('index.html', imagenes=imagenes, data=data)

if __name__ == '__main__':
    app.run(debug=True)
