import sqlite3
from typing import List, Dict, Any


class DB:

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(database=self.db_path, check_same_thread=False, timeout=10)
        self.cursor = self.conn.cursor()
        self.create_table_users()
        self.create_table_images()
        print("Base de datos creada")
       

    def create_table_users(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT              
            )
        """)
        self.conn.commit()
    
    def create_table_images(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                base64_str TEXT,
                count INTEGER,
                date TEXT,
                hour TEXT
            )
        """)
        self.conn.commit()

    def insert_user(self, username: str, password: str):

        get_user = self.get_user(username)
        if get_user:
            print("Usuario ya existe")
        else:
            self.cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (?, ?)
            """, (username, password))
            self.conn.commit()

    def get_user(self, username: str) -> Dict[str, Any]:
        self.cursor.execute("""
            SELECT * FROM users WHERE username = ?
        """, (username,))
        user = self.cursor.fetchone()
        if user:
            return {
                "id": user[0],
                "username": user[1],
                "password": user[2],
            }
        return None

    def get_users(self) -> List[Dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM users
        """)
        users = self.cursor.fetchall()
        return [
            {
                "id": user[0],
                "username": user[1],
                "password": user[2],

            }
            for user in users
        ]

    def delete_user(self, username: str):
        self.cursor.execute("""
            DELETE FROM users WHERE username = ?
        """, (username,))
        self.conn.commit()

    def update_user(self, username: str, password: str):
        self.cursor.execute("""
            UPDATE users SET password = ? WHERE username = ?
        """, (password,  username))
        self.conn.commit()

    def close(self):
        self.conn.close()


    def insert_image(self, name: str, base64_str: str, count: int, date: str, hour: str):
        self.cursor.execute("""
            INSERT INTO images (name, base64_str, count, date, hour)
            VALUES (?, ?, ?, ?, ?)
        """, (name, base64_str, count, date, hour))
        self.conn.commit()

    def get_image(self, name: str) -> Dict[str, Any]:
        self.cursor.execute("""
            SELECT * FROM images WHERE name = ?
        """, (name,))
        image = self.cursor.fetchone()
        if image:
            return {
                "id": image[0],
                "name": image[1],
                "base64_str": image[2],
                "count": image[3],
                "date": image[4],
                "hour": image[5]
            }
        return None

    def get_images(self) -> List[Dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM images
        """)
        images = self.cursor.fetchall()
        return [
            {
                "id": image[0],
                "name": image[1],
                "base64_str": image[2],
                "count": image[3],
                "date": image[4],
                "hour": image[5]
            }
            for image in images
        ]
