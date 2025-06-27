import pandas as pd
import sqlite3 as sql

# 1. Carica il CSV e seleziona solo la colonna "Name"
df = pd.read_csv("pokemon.csv")
df2 = df[["Name"]]

# 2. Crea/connette il database (file .db)
conn = sql.connect("pokemon.db")

# 3. Esporta il DataFrame in una tabella SQLite chiamata "pokemon_names"
df2.to_sql("pokemon_names", conn, if_exists="replace", index=False)

# 4. (OPZIONALE) Leggi e mostra i dati appena inseriti
result = pd.read_sql("SELECT * FROM pokemon_names LIMIT 5", conn)
print(result)

# 5. Chiudi la connessione
conn.close()
