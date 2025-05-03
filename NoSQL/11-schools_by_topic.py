#!/usr/bin/env python3
""" List all topics in a school document based on the topic """


def schools_by_topic(mongo_collection, topic):
    """ List all topics in a school document based on the topic """
    return list(mongo_collection.find({"topics": topic}))
