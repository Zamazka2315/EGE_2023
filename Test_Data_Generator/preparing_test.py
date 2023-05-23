import Test_Data_Generator.work_with_csv as wrk

sourcePathCSV = "Files_with_test_data/00_indata_cases.csv"
resultPathCSV = "Files_with_test_data/01_test_data.csv"
resultPathJSON = "Files_with_test_data/02_json_data.json"
mappingPath = "Files_with_test_data/mapping_file.csv"
# Пример json-сообщения
msg = '{"cases_name":"Если[Events].collector_time>tounixtimestamp([ClientList].client_active_to_dttm)тоошибка","value":{"client_id":"12963919","id":"81027123-a3e4-420b-ab23-df052eceba05","source":"https://samokat.ru/samokat-app","type":"Catalog-Product-InstructionButtonClick","device_time":1640763478627000,"collector_time":1665853437000,"device_id":"ceb4c46d-436b-4ab8-b08b-df052eceba05","app_session_id":"ca6aa23f-0687-4836-8ee8-df052eceba05"}}'

wrk = wrk.Generator(sourcePathCSV, resultPathCSV, resultPathJSON, mappingPath, msg)
wrk.create_result_csv()
wrk.create_list_of_json()