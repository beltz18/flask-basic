from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'hello world'

@app.route('/usuarios/<usuario>')
def usuarios(usuario):
  return f'hola {usuario}'

@app.route('/clientes')
def clientes():
  return 'hola clientes'

if __name__ == '__main__':
  app.run()