import time

from bookpuller import sequential, asynchronous


def demo():
    start1 = time.time()
    sequential.run()
    end1 = time.time()

    start2 = time.time()
    asynchronous.run()
    end2 = time.time()

    print('\n\n\n')

    print(end1 - start1)
    print(end2 - start2)


if __name__ == '__main__':
    demo()