from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('Inicio.html')

@app.route('/Cantina')
def Cantina():
    return render_template('Cantina.html')

@app.route('/Fixtures')
def Fixture():
    return render_template('Fixtures.html')

@app.route('/Inscripcion')
def Inscripcion():
    return render_template('Inscripcion.html')

@app.route('/Mapa')
def Mapa():
  return render_template('Mapa.html')

@app.route('/Sponsors')
def Sponsors():
  return render_template('Sponsors.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)