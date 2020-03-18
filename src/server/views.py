from flask import Flask, request, jsonify

from .consts import DBNAME, USER, PASSWORD, HOST
from .core import work_db

app = Flask(__name__)


@app.route("/", methods=["POST"])
def check():
    event = request.get_json("event")
    act = work_db(DBNAME, USER, PASSWORD, HOST)

    if event == "save":
        act.add_data()
        return 200
    if event == "upload":
        act.upload_data()
        return 200
    if event == "delete":
        act.delete_data()
        return 200

    return 200


@app.route("/", methods=["GET"])
def check_get():
    return "Даша шулер"
