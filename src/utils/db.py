import sqlite3
import json

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, user_id, username):
        with self.connection:
            return self.cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username,))


    def user_exists(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()


    def get_all_users(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users ORDER BY score DESC').fetchall()


    def add_score(self, user_id, score):
        with self.connection:
            return self.cursor.execute('UPDATE users SET score = score + ? WHERE user_id = ?', (score, user_id,))
        

    def add_task(self, user_id, task_id):
        with self.connection:
            solved_tasks = self.cursor.execute('SELECT solved_tasks FROM users WHERE user_id = ?', (user_id,)).fetchone()
            if not solved_tasks[0]:
                tasks_list = [task_id]
            else:
                existing_tasks = json.loads(solved_tasks[0])
                existing_tasks.append(task_id)
                tasks_list = existing_tasks

            self.cursor.execute('UPDATE users SET solved_tasks = ? WHERE user_id = ?', (json.dumps(tasks_list), user_id,))


    def task_exists(self, user_id, task_id):
        with self.connection:
            row = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
            if row:
                solved_tasks_json = row[3]
                if solved_tasks_json:
                    solved_tasks = json.loads(solved_tasks_json)
                else:
                    solved_tasks = {}
                return task_id in solved_tasks
            else:
                return False


db = Database('db.db')
