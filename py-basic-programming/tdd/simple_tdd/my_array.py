class MyArray(object):
    def sum(self, size, array_str):
        numbers = [int(number) for number in array_str.split(' ')]
        if size != len(numbers):
            raise Exception('array_str은 size 크기를 가져야합니다.')
        return sum(numbers)
