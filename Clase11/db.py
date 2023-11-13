# Activar env
from pymongo import MongoClient


from clave.clave import url_db

url_db_error = "mongodb+srv://username:password@cluster0.nvlfntw.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url_db)

# list databases
print(client.list_database_names())

