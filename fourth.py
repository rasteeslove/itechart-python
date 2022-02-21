def fibonacci(n):
    """
    Get first n Fibonacci numbers.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


def DiscardLastN(g, n):
    queue = [0] * n
    counter = 0
    for i in g:
        if counter >= n:
            yield queue[counter % n]
        queue[counter % n] = i
        counter += 1


def demo():
    H = 42
    print(list(fibonacci(H)))
    print('\n\n')

    my_list = [1, 3, 6, 10]
    discarded = DiscardLastN(g = (x for x in my_list), n = 2)
    for i in discarded:
        print(i, end=' ')
    print('\n\n')    

    discarded2 = DiscardLastN(fibonacci(42), n = 33)
    for i in discarded2:
        print(i, end=' ')


if __name__ == '__main__':
    demo()
