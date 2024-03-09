import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, user_id, username):
        with self.connection:
            return self.cursor.execute('INSERT INTO "users" ("user_id", "username") VALUES (?, ?)', (user_id, username,))


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            return bool(len(result))


    def get_users(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "users" ORDER BY "score" DESC').fetchall()
            return result


    def add_score(self, user_id, score):
        with self.connection:
            return self.cursor.execute('UPDATE users SET "score" = "score" + ? WHERE user_id = ?', (score, user_id,))


db = Database('db.db')
