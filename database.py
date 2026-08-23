import sqlite3

connection = sqlite3.connect("reflections.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reflections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    raw_text TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    stressors TEXT,
    emotions TEXT,
    avoidance_flag INTEGER DEFAULT 0,
    concerning_signal_flag INTEGER DEFAULT 0
)
""")

connection.commit()
connection.close()

print("Database created successfully!")
