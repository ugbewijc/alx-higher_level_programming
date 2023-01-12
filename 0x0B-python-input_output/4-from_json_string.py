#!/usr/bin/python3

"""Defines From JSON string to Object Function"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
