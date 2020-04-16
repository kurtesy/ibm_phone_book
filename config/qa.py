import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = 'phonebook_qa.db'
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
target_path = os.path.join(PROJECT_ROOT, 'database')

# Build the Sqlite URL for SqlAlchemy
sqlite_url = "sqlite:///" + os.path.join(target_path, DB_NAME)

# SqlAlchemy Config
db = sqlalchemy.create_engine(sqlite_url, echo=True)
meta = sqlalchemy.MetaData()
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()
