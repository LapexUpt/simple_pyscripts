import pandas as pd
"""
Считывает два csv-файла original.csv и compare.csv, преобразует их в множества. 
Для сравнения берет в каждом файле столбцы, номера которых указаны в value[...] (отсчет с 0).
Выводит неуникальные значения списком.
"""
original_file = pd.read_csv('original.csv', sep=';')
compare_file = pd.read_csv('compare.csv', sep=';')
result=list(set((value[1]) for value in compare_file.values) & set((value[1]) for value in original_file.values))
print(result)