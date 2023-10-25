import json


def import_json(json_file):
    """возвращает json-строку из json-файла"""
    with open(json_file, "r") as file:
        return json.load(file)


a = import_json("operations.json")
print(a)


def add_date(dictionary):
    date_dict = []
    ready_date_dict = []
    for i in range(0, len(dictionary)):
        for k in dictionary[i].items():
            date_dict.append(dictionary[i]["date"])
    for i in range(0, len(date_dict)):
        ready_date_dict.append(date_dict[i][0:10])
    # return ready_date_dict
    return date_dict


print(add_date(a))
