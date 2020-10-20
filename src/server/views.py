from flask import Flask, request, jsonify

from .handler import MainHandler
from .utils import parse_args

app = Flask(__name__)


@app.route("/", methods=["POST"])
def check():
    login, password, host, dbname = parse_args()
    resp = request.get_json()
    act = MainHandler(dbname, login, password, host)

    if resp["event"] == "save":

        data_to_save = resp["to_save"]

        result = act.add_data(data_to_save)

        if result == True:
            return {"result": "data insert in database"}
        else:
            return {"result": "error"}

    if resp["event"] == "upload":
        act.upload_data()
        return 200

    if resp["event"] == "delete":
        act.delete_data()
        return 200

    return 200


@app.route("/", methods=["GET"])
def check_get():
    return "Ashot PIDARAS"
