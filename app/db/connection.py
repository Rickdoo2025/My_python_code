import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Make sure this is called before getenv

def get_db_connection():
    try:
        db_host = os.getenv("DB_HOST", "127.0.0.1")
        db_port = os.getenv("DB_PORT", "3306")  # ✅ Always default to string
        db_user = os.getenv("DB_USER","root")
        db_pass = os.getenv("DB_PASSWORD","Ronish@2025!")
        db_name = os.getenv("DB_NAME","sakila")

        print("🧪 Loaded from .env →", db_host, db_port, db_user, db_name)

        if not all([db_user, db_pass, db_name]):
            raise ValueError("One or more required environment variables are missing.")

        conn = mysql.connector.connect(
            host=db_host,
            port=int(db_port),  # ✅ This will work now
            user=db_user,
            password=db_pass,
            database=db_name
        )
        print("✅ Connected to DB successfully.")
        return conn

    except Exception as e:
        print("❌ Database connection error:", e)
        return None
