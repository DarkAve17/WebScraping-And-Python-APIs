from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from config import POSTGRES_CONFIG

#password = os.environ.get('PGPASSWORD')
#connection_string = f'postgresql://postgres:{password}@localhost:5432/PULL Test'


URL_DATABASE = f"postgresql://{POSTGRES_CONFIG['username']}:{POSTGRES_CONFIG['password']}@{POSTGRES_CONFIG['host']}:{POSTGRES_CONFIG['port']}/{POSTGRES_CONFIG['database']}"
#URL_DATABASE = 'postgresql://postgres:4b4aK3%401@localhost:5432/PULL Test'


engine= create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)

Base = declarative_base()