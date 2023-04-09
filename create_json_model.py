import json
""""
Считывает из файла id_file.csv строки.
Создает json-модель нужного формата.
Записывает json модель в файл json_model.csv для дальнейшей обработки.
"""
result_list = []
 
with open('id_file.csv', 'r') as id_file:
    for val in id_file.readlines():
        result_dict = dict()
        result_dict["type"] = "Id"
        if val.endswith('\n'):
            result_dict["value"] = val[:-1]
        else:
            result_dict["value"] = val
        result_list.append(result_dict)
 
result = json.dumps(result_list)

with open('json_model.csv', 'w') as model_file:
    model_file.write(result)