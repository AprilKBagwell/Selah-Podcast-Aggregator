
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Wywuasmndwya1!",  # Replace with your MySQL root password
        database="selah_podcast"
        
    )
