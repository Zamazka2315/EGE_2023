import csv
import random
import uuid
import datetime
import string
import json

class Generator:
    def __init__(self, sourcePathCSV, resultPathCSV, resultPathJSON, mappingPath, msg):
        self.sourcePathCSV = sourcePathCSV
        self.resultPathCSV = resultPathCSV
        self.resultPathJSON = resultPathJSON
        self.mappingPath = mappingPath
        # Пример json-сообщения
        self.msg = msg

    def list_of_dict(self, path: str) -> list:
        with open(path) as csv_file:
            dict_reader = csv.DictReader(csv_file)
            list_of_dict = list(dict_reader)
        csv_file.close()
        return list_of_dict

    def generate_test_data(self, type: str):
        type = type.lower()  # нет чувствительности к регистру
        if type == 'uuid':              return str(uuid.uuid4())
        if type == 'timestamp':         return datetime.datetime.now().isoformat() + 'Z'
        if type == 'unixTimestamp':     return int(datetime.datetime.now().timestamp())
        if type == 'date':              return str(datetime.datetime.now().date())
        if type == 'string':            return ''.join(random.choice(string.ascii_lowercase) for i in range(15))
        if type == 'boolean':           return random.randint(0, 1)
        if type == 'float':             return random.uniform(0, 100)
        if type == 'integer':           return random.randint(-2147483648, 2147483648)
        if type == 'bigint':
            return random.randint(-9223372036854775808, 9223372036854775808)
        else:
            return type

    # Создает лист со сгенерированными полями из csv-источника
    def generate_dicts_with_new_data(self, source_list:list):
        result_list = list()
        for l in source_list:
            result_dict = {}
            l = dict(l)
            for k in l.keys():
                result_dict.update(
                    {
                        k: self.generate_test_data(l[k])
                    }
                )
            result_list.append(result_dict)
        return result_list

    def list_of_dictionaries_to_csv(self, list_of_dict:list, path: str):

        with open(path, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, list_of_dict[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(list_of_dict)
        output_file.close()


    def json_check_type_of_field(self, source_json:dict, key_json:str, value_json:str, list_of_map:list):
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

    def json_generate_with_msg(self, d_result: dict, d_source_with_csv: dict, list_of_map:list):
        for key, value in list(d_result.items()):
            if key in d_source_with_csv.keys():
                if d_source_with_csv[key] == "del": del d_result[key]
                else:
                    self.json_check_type_of_field(d_result, key, d_source_with_csv[key],list_of_map)
            elif type(value) == list:
                if type(value[0]) == dict:
                    self.json_generate_with_msg(value[0],d_source_with_csv,list_of_map)
            elif isinstance(value, dict):
                self.json_generate_with_msg(value,d_source_with_csv,list_of_map)
        return d_result

    def create_list_of_json(self):
        map_list = self.list_of_dict(self.mappingPath)
        sorce_dict = self.list_of_dict(self.resultPathCSV)
        resul_json={}
        with open(self.resultPathJSON, 'w', encoding='utf-8') as jsonf:

            for row in sorce_dict:
                json_draft = json.loads(self.msg)
                resul_json=self.json_generate_with_msg(json_draft, row, map_list)

                jsonString = json.dumps(resul_json, indent=4, )
                jsonf.write(jsonString.replace("\n", "").replace(" ", "") + ',' + "\n")




    def create_result_csv(self):
        #     1 Получить словарь из источника
        source_dict = self.list_of_dict(self.sourcePathCSV)
        #     2 Генерирум тестовые данные
        result_dicts = self.generate_dicts_with_new_data(source_dict)
        #     3 Положить словари в файл
        self.list_of_dictionaries_to_csv(result_dicts, self.resultPathCSV)
