def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, ** kwargs)
        print(result)
        if result != 1 and ( result % result ) == 0:
            print("Число простое")
        else:
            print("Число не простое")
    return wrapper


@is_prime
def sum_three(*arg):
    return sum(arg)

result = sum_three(2, 3, 6)
print(result)
