# Workaround for sqlite3 issue in some environments
import sys

__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb

# Initialize and return a Chromadb Client
def get_chromadb_client():
    return chromadb.Client()
