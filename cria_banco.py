import sqlite3

connection = sqlite3.connect('bancochillplace.db')
cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
    nome text, estrelas real, diaria real, cidade text)"

criar_hotel = "INSERT INTO hoteis VALUES ('alpha', 'alpha Hotel', 4.3, 345.30, 'Rio de janeiro')"
cursor.execute(criar_tabela)
cursor.execute(criar_hotel)
connection.commit()
connection.close()