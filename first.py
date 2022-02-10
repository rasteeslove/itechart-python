import copy


def my_sum(*args):
    s = 0
    for arg in args:
        try:
            s += arg
        except:
            pass
    return s


def foo1(foo, *args):
    return foo(*args)


def foo2(*args):
    return ''.join(filter(lambda x: type(x) == str, args))


def foo3(*args):
    return ' '.join(filter(lambda x: type(x) == str, args))


def printfunc(func):
    def run_and_print(*args):
        print(func(*args))
    return run_and_print


def foo7(*args, **kwargs):
    for _, kwarg in kwargs.items():
        if callable(kwarg):
            kwarg(*args)


def demo():
    
    # 0:
    my_dict = {
        "first_key": "first_value",
        "second_key": "second_value",
        "third_key": "third_value"
    }

    # 1:
    new_dict = {val: key for key, val in my_dict.items()}
    print(my_dict)
    print(new_dict)
    print('\n\n\n')

    # 2:
    my_dict_keys = list(my_dict.keys())
    print(my_dict_keys)
    print('\n\n\n')

    # 3:
    keys1 = [42, 'hello', None, 'apple', 'banana']
    values1 = ['20', type(type), True, 'pie', 3.14]
    dict1 = {key: val for key, val in zip(keys1, values1)}
    print(dict1)
    print('\n\n\n')

    # 4:
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square_lambda = lambda x: x**2
    list2 = [square_lambda(el) for el in list1]
    print(list1)
    print(list2)
    print('\n\n\n')

    # 5:
    list3 = [15, 96, 'potato', 0.33, list1, 300, 2.22]
    print(my_sum(*list3))
    print('\n\n\n')

    # 6:
    print(foo1(foo2, 'hello', ' ', 'world'))
    print(foo1(foo3, 'hello', 'world'))
    print('\n\n\n')

    # 7:
    foo7(28, 'never', False, 3.6, 2.7, 'the', -77, set([1, 2, 3]), 'less', 50.5, func1=printfunc(foo2), func2=printfunc(foo3), func3=printfunc(my_sum), kwarg1=42, kwarg2='banana')


if __name__ == '__main__':
    demo()
