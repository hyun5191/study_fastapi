import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.jason(BASE_DIR, 'secret.jason')
secrets = json.loads(open(SECRET_FILE).READ())

DB = secrets["DB"]
DB_URL = f"mysql+pymysql://{DB['user']}:{DB['passwprd']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_engine(
    DB_URL, encoding='utf-8'
)

local_session = sessionmaker(autocomit=False, autoflush=False, bind=engine)
base = declarative_base()