import sqlite3
from typing import Any, Dict, List

class ImagesDB:
        
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                base64_str TEXT
            )
        """)
        self.conn.commit()
    
    def insert_image(self, name: str, base64_str: str):
        self.cursor.execute("""
            INSERT INTO images (name, base64_str)
            VALUES (?, ?)
        """, (name, base64_str))
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
                "base64_str": image[2]
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
                "base64_str": image[2]
            }
            for image in images
        ]
    
    