#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo-service")

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except Exception as e:
        return f"Error connecting to MongoDB: {e}"
    return "Hello from the MongoDB client!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

