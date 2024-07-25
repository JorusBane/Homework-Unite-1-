calls = 0
def count_call ():
    print(calls)
def string_info (strk):
    global calls
    long = len(strk)
    str__ = strk.upper()
    str_ = strk.lower()
    calls += 1
    print(f"{long}, {str__}, {str_}")
def is_contains (string, list_to_search):
    search_ = False
    for i in list_to_search:
        str_ = string.upper()
        str__ = i.upper()
        search = str_ in str__
        if search:
            search_ = True
    global calls
    calls += 1
    return search_
string_info("Преподаватель")
print(is_contains('Dota2', ['DOTA2', 'DoT2', 'lEAGUE OF LEGENDS']))
print(is_contains('Mother', ['Mom', 'MaTh', "MeMory"]))
print(calls)


