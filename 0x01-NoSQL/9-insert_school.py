#!/usr/bin/python3
""" This module contains a function insert_school """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    return mongo_collection.insert_one(kwargs)
