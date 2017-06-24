""" Module for serialization """

import pickle
import yaml
import json

def load(file, config):
    """ deserialization """
    if config == "pickle":
        return pickle.load(file)
    elif config == "yaml":
        return yaml.load(file)
    elif config == "json":
        return json.load(file)



def save(data, file, config):
    """ serialization """
    try:
        if config == "pickle":
            pickle.dump(data, file)
        elif config == "yaml":
            yaml.dump(data, file, default_flow_style=False)
        elif config == "json":
            json.dump(data, file)
    except ValueError:
        raise Exception("[ERROR]::Serialization failed")

