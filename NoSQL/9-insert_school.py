#!/usr/bin/env python3


def insert_school(mongo_collection, **kwargs):
    """ Instert a new document in a collection """
    result = mongo_collection.insert(kwargs)
    return result.inserted_id
