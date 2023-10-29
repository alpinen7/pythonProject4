import json
import datetime


def get_json(json_file):
    """возвращает json-строку из json-файла"""
    with open(json_file, "r") as file:
        return json.load(file)


a = get_json("operations.json")
# print(len(a))


def get_executed_operations(operations_list: list):
    """выдает список список операций со статусом EXECUTED"""
    executed_operations = []
    for operation in operations_list:
        if "state" in operation and operation["state"] == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_last_operations(operations_list: list, operations_count: int):
    """выдает последние несколько операций, отстортированные от самой актуальной операции"""
    sorted_operations = sorted(operations_list, key=lambda operation: operation["date"], reverse=True)
    last_operations = sorted_operations[0:operations_count]
    return last_operations

def get_correct_date(operations_list: list):
    """конвертирует формат даты в формат дд.мм.гггг"""
    for operation in operations_list:
        if "date" in operation:
            operation["date"] = datetime.date(int(operation["date"][0:4]), int(operation["date"][5:7]), int(operation["date"][8:10]))
            operation["date"] = datetime.date.strftime(operation["date"], '%d.%m.%Y')
    return operations_list


def get_correct_inform(operations_list: list):
    operations_formatted_list = []
    for operation in operations_list:
        description = operation["description"]
        if "from" in operation:
            payer = operation["from"].split()
            payment_method = payer.pop()
            if "Счет" == payer[0]:
                payment_method_from = f"**{payment_method[-4:]}"
            else:
                payment_method_from = f"{payment_method[0:4]} {payment_method[4:6]}** **** {payment_method[-4:]}"
            payer_info = " ".join(payer)
        if "to" in operation:
            recipient = operation["to"].split()
            recipient_method = recipient.pop()
            if "Счет" == recipient[0]:
                recipient_method_to = f"**{recipient_method[-4:]}"
            else:
                recipient_method_to = f"{recipient_method[0:4]} {recipient_method[4:6]}** **** {recipient_method[-4:]}"
            recipient_info = " ".join(recipient)
        operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        operations_formatted_list.append(f"{get_correct_date(operations_list)} {description}\n{payer_info} {payment_method_from}"
                                         f" -> {recipient_info} {recipient_method_to}\n{operation_amount}")

