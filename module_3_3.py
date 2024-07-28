def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params("Privet", False)
print_params(True)
print_params()
value_list = [10, "String2", False]
print_params(*value_list)
print_params(b = 25)
print_params(c = [1,2,3])
value_dict = {"a": "091",
              "b": True,
              "c": 21}
print_params(**value_dict)
value_list2 = [29, True]
print_params(*value_list2, 42)
