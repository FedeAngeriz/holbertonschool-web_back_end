#!/usr/bin/env python3
""" Update the topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ Update the topics of a school document based on the name """
    mongo_collection.updateMany(
        {"name": name},
        {"$set": {"topics": topics}}
    )
