import hashlib

import psycopg2


class work_db(object):
    def __init__(self, dbname, user, password, host):

        self.conn = psycopg2.connect(
            dbname="main", user="artyom", password="P@ssw0rd", host="localhost"
        )
        self.cursor = self.conn.cursor()

    def add_data(self, data: dict):
        try:

            data["password"] = self._cryptoPassword(data["password"])

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

    def _cryptoPassword(self, password):
        password = password.encode()
        crypto_password = hashlib.sha256(password).hexdigest()

        return crypto_password

    def upload_data(self):
        return 200

    def delete_data(self):
        return 200
