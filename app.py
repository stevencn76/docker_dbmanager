import sqlalchemy
import os


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_DATABASE = os.getenv("DB_DATABASE", "mydb")

engine = sqlalchemy.create_engine(f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}')
with engine.connect() as conn:
    query = sqlalchemy.text('SELECT @@version')
    result_set = conn.execute(query)

    print("MySQL version:")
    for row in result_set:
        print(row)

engine.dispose()
