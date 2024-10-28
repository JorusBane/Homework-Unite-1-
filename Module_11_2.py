import inspect
from pprint import pprint
def inrospection_info(obj):
    pprint(f"Тип объекта: {type(obj)}")
    pprint(f"Методы и Аттрибуты: {dir(obj)}")
    pprint(f"Модуль, к которому принадлежит объект: {inspect.getmodule(obj)}")

number_info = inrospection_info(42)
number_info