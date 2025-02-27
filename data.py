
import pandas as pd
from sqlalchemy import create_engine

# Charger le fichier CSV
df = pd.read_csv('./DataSvc/shoes_fact.csv')

# Créer une connexion avec SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:talom.2005@@localhost:5432/dataScience')

# Insérer les données dans la table
df.to_sql('adidas', engine, if_exists='replace', index=False)
