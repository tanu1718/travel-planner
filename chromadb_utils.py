# Workaround for sqlite3 issue in some environments
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb
from chromadb.config import Settings
import os

# Initialize and return a Chromadb Client
def get_chromadb_client():
    # Define the persistence directory
    persist_directory = os.path.join(os.getcwd(), "chroma_db")  # Persistent directory for ChromaDB

    # Create and return the ChromaDB client
    return chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",  # Default implementation
        persist_directory=persist_directory  # Set to None for in-memory database
    ))
