from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/practice_fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta = MetaData()

conn = engine.connect()



