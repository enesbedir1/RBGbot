import ruamel.yaml
import sys
from character import character

def read_characters(path, dict):
    yaml = ruamel.yaml.YAML()
    yaml.register_class(character)
    with open(path, "r") as stream:
        ch_lists = yaml.load(stream)
        if ch_lists is not None:
            for ch in ch_lists:
                dict[ch.name] = ch

def write_characters(path, dict):
    yaml = ruamel.yaml.YAML()
    yaml.register_class(character)
    with open(path, 'w') as f:
        yaml.dump(list(dict.values()), f)

def setattr_qualified(obj, name, value):
    parts = name.split(".")
    for attr in parts[:-1]:
        obj = getattr(obj, attr)
    setattr(obj, parts[-1], type(getattr(obj, parts[-1]))(value))
