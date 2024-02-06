from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Lista de nombres de imágenes para pasar a la plantilla HTML
    imagenes = ['imagen1.jpg', 'imagen2.jpg']  # Agrega más imágenes si es necesario
    return render_template('index.html', imagenes=imagenes)

if __name__ == '__main__':
    app.run(debug=True)
