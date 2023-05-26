import os

import psycopg2
from dotenv import load_dotenv


class DatabaseInterface:
    load_dotenv()

    def __init__(self):
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.database = os.getenv("DB")
        self.user = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
        return self.connection

    def execute_query(self, query):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def fetch_data(self, query):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
