import os
import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

def get_connection():
    return psycopg.connect(
        dbname="postgres", #os.getenv("DB_NAME"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "Admin@123"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        row_factory=dict_row, #type ignore
        #autocommit=True usado para criar database
    )

def test_connection():
    #get_connection().cursor().execute("CREATE DATABASE books;") usado para criar database
    print(get_connection().cursor().execute("SELECT version()"))

test_connection()