from flask import Flask, request
from flask_cors import CORS

from study_buddy_app.repository_g612 import connect_to_database, database, create_user, get_user_password

app = Flask("UsersAPI")
CORS(app)


@app.route('/api/v1/sign-up', methods=["POST"])
def signup():
    try:
        body = request.json
        conn = connect_to_database(database)
        create_user(conn, body)
        conn.close()
        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to create user. Message: {e}"
        }
        return error, 500


@app.route('/api/v1/sign-in', methods=["POST"])
def sign_in():
    # extragem body-ul din request
    body = request.json

    # extragem detaliile (email, parola) din body-ul request-ului
    email = body.get("email", None)
    if email is None:
        error = {
            "error": "--Failed to sign in. Missing email."
        }
        return error, 400

    password = body.get("password", None)
    if password is None:
        error = {
            "error": "--Failed to sign in. Missing password."
        }
        return error, 400

    # verifica daca user-ul (email) exista in baza de date.
    # 1. extragem din baza de date parola user-ului cu email-ul primit
    try:
        conn = connect_to_database(database)
        existing_password = get_user_password(conn, email)
    except Exception as e:
        error = {
            "error": f"--Failed to sign in. Message: {e}"
        }
        return error, 500

    # 2. daca utilizatorul nu exista => parola nu exista (None) => returnam un mesaj de eroare
    if existing_password is None:
        error = {
            "error": "--Failed to sign in. Invalid email or password."
        }
        return error, 401

    # 3. data utilizatorul exista => parola == string => mergem la urmatorul pas
    # 4. verificam daca parola din baza de date == parola primita de la client
    # 5. daca parolele sunt diferite => returnam un mesaj de eroare
    if password != existing_password:
        error = {
            "error": "--Failed to sign in. Invalid email or password."
        }
        return error, 401

    # 6. daca parolele sunt identice => returnam un mesaj fara body, status = 204
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=3012)