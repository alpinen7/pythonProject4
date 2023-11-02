from src import utils


def test_get_json():
    assert len(utils.get_json('operations.json')) > 0


def test_get_executed_operations(test_data):
    assert len(utils.get_executed_operations(test_data)) == 4


def test_get_last_operations(test_data):
    assert utils.get_last_operations(test_data, 1) == [{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2023-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  }]


def test_get_correct_date(test_data):
    assert utils.get_correct_date(test_data) == ["26.08.2019", "03.07.2019", "30.06.2018", "23.03.2018", "04.04.2023"]


def test_get_correct_inform(test_data):
    assert utils.get_correct_inform(test_data)[0] == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199-> Счет **9589\n31957.58 руб.'

