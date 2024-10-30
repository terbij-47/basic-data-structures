def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
# inner_function() <- возникает ошибка "name 'inner_function' is not defined"

test_function()
