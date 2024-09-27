from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('menu.html')

@app.route('/Cantina')
def Cantina():
    return render_template('Cantina.html')

if __name__ == '__main__':
    app.run(debug=True, port=3500)