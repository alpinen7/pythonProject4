import utils

operations_file = utils.get_json("operations.json")
executed_operations = utils.get_executed_operations(operations_file)
last_operations = utils.get_last_operations(executed_operations, 5)
correct_information = utils.get_correct_inform(last_operations)
print(correct_information)