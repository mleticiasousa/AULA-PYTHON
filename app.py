from flask import Flask

#Objeto/servidor do flask
app = Flask(__name__)

#rota principal
@app.route('/')
def hello():
     return "Olá Mundo!"
 
 #execução do servidor
if __name__ == "__main__":
    app.run(debug=True)