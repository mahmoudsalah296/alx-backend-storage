#!/usr/bin/env python3
"""MongoDB with python"""


def list_all(mongo_collection):
    """list all documents in a collection"""
    return mongo_collection.find()
