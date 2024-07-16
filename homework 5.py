immutable_var = 'a', 2, True, 3.5
print(immutable_var)
#immutable_var [0] = 'b'
#print(immutable_var) - immutable_var - это кортеж, который является неизменяемым объектом
immutable_var = [10, 23], 'a', True, 3.8
immutable_var [0][1] = 49
print(immutable_var) # Но кортеж может содержать в себя изменяемый объект
mutable_list = ["Russia", False, 2024]
print(mutable_list)
mutable_list[0] = "France"
mutable_list[2] = 2005
print(mutable_list)
