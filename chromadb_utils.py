# Workaround for sqlite3 issue in some environments
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb
from chromadb.config import Settings
import os

# Initialize and return a ChromaDB client
def get_chromadb_client():
    # Specify the persistence directory
    persist_directory = os.path.join(os.getcwd(), "chroma_db")  # Persistent directory for ChromaDB

    # Use the updated client initialization
    client = chromadb.Client(Settings(
        chroma_api_impl="local",          # Specify local API implementation
        persist_directory=persist_directory  # Directory for data persistence
    ))
    return client
