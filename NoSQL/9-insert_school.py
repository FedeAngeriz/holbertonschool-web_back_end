#!/usr/bin/env python3
""" Instert a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ Instert a new document in a collection """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
