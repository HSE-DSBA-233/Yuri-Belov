import sqlite3
import json

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, user_id, username):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchall()
            if not result:
                self.cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username,))


    def get_all_users(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users ORDER BY score DESC').fetchall()
            return result


    def add_score(self, user_id, score):
        with self.connection:
            return self.cursor.execute('UPDATE users SET score = score + ? WHERE user_id = ?', (score, user_id,))


    def add_tasks(self, user_id, task_id):
        with self.connection:
            self.cursor.execute('SELECT tasks FROM users WHERE user_id = ?', (user_id,))
            existing_tasks = self.cursor.fetchone()
            
            if existing_tasks is None:
                tasks_list = [task_id]
            else:
                existing_task_ids = json.loads(existing_tasks[0])
                existing_task_ids.append(task_id)
                tasks_list = existing_task_ids

            # Update the tasks for the user
            self.cursor.execute('UPDATE users SET tasks = ? WHERE user_id = ?', (json.dumps(tasks_list), user_id,))


db = Database('db.db')
