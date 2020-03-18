import psycopg2


class work_db(object):
    def __init__(self, dbname, user, password, host):
        conn = psycopg2.connect(
            dbname="main", user="artyom", password="P@ssw0rd", host="localhost"
        )
        self.cursor = conn.cursor()

    def add_data(self):
        return 200

    def upload_data(self):
        return 200

    def delete_data(self):
        return 200
