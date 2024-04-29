#!/usr/bin/env python3
""" This module contains a script"""

from pymongo import MongoClient

if __name__ == "__main__":
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient("mongodb://127.0.0.1:27017")

    print(f"{client.logs.nginx.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(
            f"\tmethod {method}: {client.logs.nginx.count_documents({'method': method})}"
        )
    print(
        f"{client.logs.nginx.count_documents({'method': 'GET', 'path': '/status'})} status check"
    )
