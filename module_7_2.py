def custom_write(file_name, string):
    file_name = "test_file.txt"
    file = open(file_name, 'w', encoding= 'utf-8')
    string_positions = {}
    count = 0
    for i in string:
        string_positions.update({(count, file.tell()): i})
        file.write(i + "\n")
        count += 1
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)