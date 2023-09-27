from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine("sqlite:///european_database.sqlite")
engine = create_engine("postgresql+psycopg2://myalchemy:mypass@localhost:5432/mysqlachemy", echo=False)
conn = engine.connect() 

Session = sessionmaker(bind=engine)

# Créez une instance de session
session = Session()