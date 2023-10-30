import utils

user_input = int(input("введите число последних операций: "))
operations_file = utils.get_json("operations.json")
# print(operations_file)
executed_operations = utils.get_executed_operations(operations_file)
# print(executed_operations)
last_operations = utils.get_last_operations(executed_operations, user_input)
# print(last_operations)
correct_information = utils.get_correct_inform(last_operations)
# print(correct_information)
for i in range(user_input):
    print(f"{correct_information[i]}\n")
    # print()
# print(utils.get_correct_date(utils.get_json("operations_traning.json")))
# print(correct_information)