import streamlit as st
import sqlite3
from datetime import datetime

st.title("Mental Health AI")

student_id = "student_001"

reflection = st.text_area(
    "What's going on?",
    placeholder="Write whatever has been on your mind..."
)

if st.button("Save Reflection"):

    if reflection.strip():

        connection = sqlite3.connect("reflections.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO reflections
        (student_id, raw_text, timestamp)
        VALUES (?, ?, ?)
        """, (
            student_id,
            reflection,
            datetime.now().isoformat()
        ))

        connection.commit()
        connection.close()

        st.success("Reflection saved.")

    else:
        st.warning("Please write something first.")
        