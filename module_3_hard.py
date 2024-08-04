def check_dict (dict_elem):
    dict_result = len(dict_elem.items())
    return dict_result

def calculate_structure_sum (*args):
    if data_structure != None:
        count = 0
        if isinstance((data_structure[count]), dict) :
            result = check_dict(data_structure[count])
        elif len(data_structure[count]) > 1:
            result = sum(data_structure[count])
            data_structure[count].pop()
        else:
            result = data_structure[count].pop()
    return result + calculate_structure_sum(*args)



data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)
