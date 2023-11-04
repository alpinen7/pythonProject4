import utils

user_input = int(input("введите число последних операций: "))
operations_file = utils.get_json("operations.json")
executed_operations = utils.get_executed_operations(operations_file)
last_operations = utils.get_last_operations(executed_operations, user_input)
correct_information = utils.get_correct_inform(last_operations)
for i in range(user_input):
    print(f"{correct_information[i]}\n")