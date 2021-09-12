class MyException(Exception):
    def __init__(self, e):
        super().__init__('{0}으로 나눌 수 없습니다.'.format(e))


def division(x, y):
    if y != 0:
        return x / y
    else:
        raise MyException(y)


try:
    result = division(10, 2)
    print('result: {0}'.format(result))

except MyException as ex:
    print('예외 발생 : {0}'.format(ex))
else:
    print('정상 실행!!')
finally:
    print('항상 실행!!')

try:
    result = division(10, 0)
    print('result: {0}'.format(result))

except MyException as ex:
    print('예외 발생 : {0}'.format(ex))
else:
    print('정상 실행!!')
finally:
    print('항상 실행!!')
