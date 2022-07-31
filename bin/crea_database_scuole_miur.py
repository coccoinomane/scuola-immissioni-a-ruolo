"""
Esegui questo script per popolare il database sqlite3
con gli indirizzi delle scuole presi da OpenData
"""
from src.helpers.sqlite3 import crea_database_scuole_miur

crea_database_scuole_miur()
