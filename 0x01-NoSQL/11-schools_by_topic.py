#!/usr/bin/env python3
""" This module contains a function schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    return mongo_collection.aggregate([{"$match": {"topics": topic}}])
