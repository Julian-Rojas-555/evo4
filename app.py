from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "evofitsor_secret_key"

# MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))
db = client["evofitsor"]
users_collection = db["users"]

# Dietas y rutinas
plans = {
    "bajar_grasa": {
        "dieta": """
Desayuno:
- 3 claras y 1 huevo entero
- Avena con fruta

Almuerzo:
- Pechuga de pollo
- Arroz integral
- Vegetales

Cena:
- Pescado o pollo
- Ensalada verde
        """,

        "rutina": """
Lunes: Cardio 30 min + Piernas
Martes: Espalda y Bíceps
Miércoles: Cardio 40 min
Jueves: Pecho y Tríceps
Viernes: Full Body
Sábado: Cardio suave
Domingo: Descanso
        """
    },

    "ganar_musculo": {
        "dieta": """
Desayuno:
- 4 huevos
- Avena
- Banano

Almuerzo:
- Carne magra
- Arroz
- Frijoles

Cena:
- Pollo
- Papa cocida
- Vegetales
        """,

        "rutina": """
Lunes: Pecho
Martes: Espalda
Miércoles: Piernas
Jueves: Hombros
Viernes: Brazos
Sábado: Abdomen
Domingo: Descanso
        """
    },

    "recomposicion": {
        "dieta": """
Desayuno:
- Huevos
- Pan integral
- Fruta

Almuerzo:
- Pollo
- Arroz
- Vegetales

Cena:
- Atún
- Ensalada
        """,

        "rutina": """
Lunes: Full Body
Martes: Cardio
Miércoles: Full Body
Jueves: Cardio
Viernes: Full Body
Sábado: Cardio ligero
Domingo: Descanso
        """
    }
}

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register_user", methods=["POST"])
def register_user():

    username = request.form["username"]
    password = request.form["password"]

    existing = users_collection.find_one({"username": username})

    if existing:
        return "Usuario ya existe"

    users_collection.insert_one({
        "username": username,
        "password": password
    })

    return redirect("/")


@app.route("/login_user", methods=["POST"])
def login_user():

    username = request.form["username"]
    password = request.form["password"]

    user = users_collection.find_one({
        "username": username,
        "password": password
    })

    if user:
        session["user"] = username
        return redirect("/dashboard")

    return "Credenciales incorrectas"


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")


@app.route("/generate", methods=["POST"])
def generate():

    if "user" not in session:
        return redirect("/")

    objetivo = request.form["objetivo"]

    result = plans[objetivo]

    return render_template(
        "results.html",
        dieta=result["dieta"],
        rutina=result["rutina"]
    )


@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)