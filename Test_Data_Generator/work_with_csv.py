import csv
import random
import uuid
import datetime
import string
import json


def generate_test_data(type_of_filed: str):
    """
    По типу данных type_of_filed рандомно генерирует значение
    Если типа нет в генераторе, оставляет как есть
    """
    type_of_filed = type_of_filed.lower()  # нет чувствительности к регистру
    if type_of_filed == 'uuid':              return str(uuid.uuid4())
    if type_of_filed == 'timestamp':         return datetime.datetime.now().isoformat() + 'Z'
    if type_of_filed == 'unixTimestamp':     return int(datetime.datetime.now().timestamp())
    if type_of_filed == 'date':              return str(datetime.datetime.now().date())
    if type_of_filed == 'string':            return ''.join(
        random.choice(string.ascii_lowercase) for i in range(15))
    if type_of_filed == 'boolean':           return random.randint(0, 1)
    if type_of_filed == 'float':             return random.uniform(0, 100)
    if type_of_filed == 'integer':           return random.randint(-2147483648, 2147483648)
    if type_of_filed == 'bigint':
        return random.randint(-9223372036854775808, 9223372036854775808)
    else:
        return type_of_filed


def list_of_dict(path: str) -> list:
    """"
    На вход подается адрес csv файла
    Берет все строки из файла и формирует словарь dict
    Возвращает список словарей
    """
    with open(path) as csv_file:
        dict_reader = csv.DictReader(csv_file)
        list_dict = list(dict_reader)
    csv_file.close()
    return list_dict


def generate_dicts_with_new_data(source_list: list):
    """
    :param source_list: На вход подается лист с {ключ:тип_данных}
    :return: Возвращает лист со словарями, где ключ остается как есть, а value генерируется {ключ:рандом}
    """
    result_list = list()
    for l in source_list:
        result_dict = {}
        l = dict(l)
        for k in l.keys():
            result_dict.update(
                {
                    k: generate_test_data(l[k])
                }
            )
        result_list.append(result_dict)
    return result_list


def list_of_dictionaries_to_csv(list_dict: list, path: str):
    """
    :param list_dict: лист со словорями
    :param path: Дирректория CSV файла, куда записать значения
    :return: построчно записывает все словари в csv файл
    """
    with open(path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, list_dict[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(list_dict)
    output_file.close()


def json_check_type_of_field(source_json: dict, key_json: str, value_json: str, list_of_map: list):
    """
    Метод проверяет key:value в правильном ли типе данных
    source_json - это из шаблона генерации сообщения
    Если значение неправильно, то обновляет
    :param source_json: исходное json сообщение, которое будет изменено
    :param key_json: Ключ, который проверяется
    :param value_json: значение, которое нужно подставить в json
    :param list_of_map: Список для маппинга
    :return: Возвращает обновленный ключ:значение
    """
    for dct in list_of_map:
        if dct["source_column"] == key_json:
            if dct["type"] in ["biginteger", "integer", "bool"] and value_json.isnumeric():
                source_json.update({key_json: bool(value_json)}) \
                    if dct["source_column"] == bool else \
                    source_json.update(
                        {key_json: int(value_json)})
            else:
                del source_json[key_json]
                source_json.update({key_json: value_json})


class Generator:

    # noinspection PyPep8Naming
    def __init__(self, source_path_CSV, result_path_CSV, result_path_JSON, mapping_path, msg):
        self.sourcePathCSV = source_path_CSV
        self.resultPathCSV = result_path_CSV
        self.resultPathJSON = result_path_JSON
        self.mappingPath = mapping_path
        # Пример json-сообщения
        self.msg = msg

    def json_generate_with_msg(self, d_result: dict, d_source_with_csv: dict, list_of_map: list):
        """
        На вход подается словарь, который нужно обновить
        При первой итерации - это self.msg пример json, на основе которого будут строиться все остальные
        :param d_result: словарь, который проверяется
        :param d_source_with_csv: Значения, которыми нужно заполнить исходный json
        :param list_of_map: Правила маппинга сообщения.
        :return:
        """
        for key, value in list(d_result.items()):
            if key in d_source_with_csv.keys():
                if d_source_with_csv[key] == "del":
                    del d_result[key]
                else:
                    json_check_type_of_field(d_result, key, d_source_with_csv[key], list_of_map)
            elif type(value) == list:
                if type(value[0]) == dict:
                    self.json_generate_with_msg(value[0], d_source_with_csv, list_of_map)
            elif isinstance(value, dict):
                self.json_generate_with_msg(value, d_source_with_csv, list_of_map)
        return d_result

    def create_list_of_json(self):
        """
        Метод формирует итоговые json и записывает построчно в файл
        :return:
        """
        map_list = list_of_dict(self.mappingPath)
        sorce_dict = list_of_dict(self.resultPathCSV)
        resul_json = {}
        with open(self.resultPathJSON, 'w', encoding='utf-8') as jsonf:
            for row in sorce_dict:
                json_draft = json.loads(self.msg)
                resul_json = self.json_generate_with_msg(json_draft, row, map_list)

                json_string = json.dumps(resul_json, indent=4, )
                jsonf.write(json_string.replace("\n", "").replace(" ", "") + ',' + "\n")

    def create_result_csv(self):
        #     1 Получить словарь из источника
        source_dict = list_of_dict(self.sourcePathCSV)
        #     2 Генерирум тестовые данные
        result_dicts = generate_dicts_with_new_data(source_dict)
        #     3 Положить словари в файл
        list_of_dictionaries_to_csv(result_dicts, self.resultPathCSV)
