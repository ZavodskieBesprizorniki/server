from flask import Flask, request, jsonify

from .consts import DBNAME, USER, PASSWORD, HOST
from .core import work_db

app = Flask(__name__)


@app.route("/", methods=["POST"])
def check():

    resp = request.get_json()
    act = work_db(DBNAME, USER, PASSWORD, HOST)

    if resp["event"] == "save":

        del resp["event"]

        result = act.add_data(resp)

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
    return "Даша шулер"
