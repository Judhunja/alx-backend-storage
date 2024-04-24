#!/usr/bin/env python3
""" This module contains a function insert_school """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs
        Return the inserted object id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
