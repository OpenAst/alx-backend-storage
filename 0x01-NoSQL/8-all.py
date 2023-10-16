#!/usr/bin/env python3
"""This script writes a 
function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """Return the list of mongo collection
        Return an empty list if nnot successful
    """
    return [doc for doc in mongo_collection.find()]
