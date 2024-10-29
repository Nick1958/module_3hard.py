# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

def calculate_structure_sum(data):
    res_sum = 0
    if isinstance(data, dict):                              # словарь
        for key, value in data.items():
            res_sum += calculate_structure_sum(key)
            res_sum += calculate_structure_sum(value)
    elif isinstance(data, str):                             # строка
        res_sum += len(data)
    elif isinstance(data, int):                             # целочисленный объект
        res_sum += data
    elif isinstance(data, (list, tuple, set)):              # список, кортеж, множество
        for item in data:
            res_sum += calculate_structure_sum(item)
    return res_sum

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),"Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
                # расчет суммы: 1 + 2 + 3 + 1 + 4 + 1 + 5 + 6 + 4 + 7 + 4 +8 + 5 + 2 + 5 + 6 + 35 = 99
