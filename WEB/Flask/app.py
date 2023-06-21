from flask import Flask
prendas = [
    {"id":1, "tipo": "psntalon", "talle": 42}
    {"id":2, "tipo": "psntalon", "talle": 56}
]
app = Flask(__name__)

@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"

@app.get("/prendas/")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas<p>"