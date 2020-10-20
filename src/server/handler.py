import hashlib

import psycopg2

from werkzeug.security import generate_password_hash


class MainHandler(object):
    def __init__(self, dbname, user, password, host):

        self.conn = psycopg2.connect(
            dbname="main", user="artyom", password="P@ssw0rd", host="localhost"
        )
        self.cursor = self.conn.cursor()

    def add_data(self, data: dict):
        try:

            data["password"] = generate_password_hash(data["password"])

            keys = []
            values = []
            for key in data:
                keys.append(key)
                values.append(data[key])

            row = ",".join(keys)
            value_to_insert = []

            for value in values:
                if type(value) == str:
                    value_to_insert.append(f"'{value}'")

                if type(value) == int:
                    value_to_insert.append(f"{value}")

            value_to_insert = ",".join(value_to_insert)

            self.cursor.execute(
                f"INSERT INTO users ({row}) VALUES ({value_to_insert});"
            )
            self.conn.commit()

            return True

        except Exception as ex:
            print(ex)
            return False

    def upload_data(self):
        return 200

    def delete_data(self):
        return 200
