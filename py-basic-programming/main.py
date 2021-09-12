import sys


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

    for path in sys.path:
        print(path)
