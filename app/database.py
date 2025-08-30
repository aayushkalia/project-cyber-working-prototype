from sqlalchemy import create_engine, Column, String, Table, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./apks.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
metadata = MetaData()

apks_table = Table(
    "apks", metadata,
    Column("apk_id", String, primary_key=True),
    Column("label", String),
    Column("explanation", String)
)

metadata.create_all(engine)
