from flask import Flask
#OOP
app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Michael",
        "last_name": "Matthews",
        "is_online": True,
        "hobbies": "traveling"
    }
    return me