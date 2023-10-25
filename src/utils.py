import json

def import_json(json_file):
    """возвращает json-строку из json-файла"""
    with open("operations.json", "r") as file:
        return json.load(file)


print(import_json("operations.json"))

