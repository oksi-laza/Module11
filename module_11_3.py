import inspect


def introspection_info(obj):
    dict_info = {}
    dict_info['type'] = type(obj).__name__
    dict_info['attributes'] = list(obj.__dict__.keys())
    dict_info['methods'] = dir(obj)
    dict_info['module'] = inspect.getmodule(obj).__name__
    dict_info['callable'] = callable(obj)  # вызываемый объект или нет
    return dict_info


class Numbers:
    def __init__(self, number1, number2, number3=8):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def amount(self):
        return self.number1 + self.number2 + self.number3

    def multiplication(self):
        return self.number1 * self.number2 * self.number3

    def max_number(self):
        return max(self.number1, self.number2, self.number3)

    def min_number(self):
        return min(self.number1, self.number2, self.number3)


numbers = Numbers(5, 15)

# Проверка кода
obj_info = introspection_info(numbers)
print(obj_info)

print('----------------------------------------------------------------------------')
obj_info_2 = introspection_info(Numbers)
print(obj_info_2)
