first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [int(len(x)) for x in first_strings if int(len(x)) > 5]
print(first_result)

second_result = [(x,y) for x in first_strings for y in second_strings  if int(len(x)) == int(len(y)) ]
print(second_result)

third_result = [{x:int(len(x))} for x in first_strings + second_strings if int(len(x)) % 2 == 0]
print(third_result)