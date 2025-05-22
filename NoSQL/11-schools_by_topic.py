#!/usr/bin/env python3
"""Module for schools_by_topic function"""


def schools_by_topic(mongo_collection, topic):
    """return"""
    return mongo_collection.find({"topics": topic})
