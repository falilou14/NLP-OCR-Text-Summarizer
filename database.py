# database.py
import sqlite3
from sqlite3 import Connection
from typing import List, Tuple

DB_PATH = "summaries.db"

def get_conn() -> Connection:
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            summary TEXT,
            translated TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_summary(text: str, summary: str, translated: str = None):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO summaries (text, summary, translated) VALUES (?, ?, ?)", (text, summary, translated))
    conn.commit()
    conn.close()

def get_all_summaries() -> List[Tuple]:
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT id, text, summary, translated, date FROM summaries ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows
