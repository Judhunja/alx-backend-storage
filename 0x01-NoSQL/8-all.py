#!/usr/bin/env python3
""" This script contains a function list_all """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ List all documents in a collections. """
    return mongo_collection.find()
