class Email:
    def __init__(self, value=None):
        self._value = value  # Переменная приватная, чтобы нельзя было просто так достать настоящий email

    def get_email(self):
        count = self._value.find('@')
        return self._value.replace(self._value[:count], 'x' * count)


class Phone_number:
    def __init__(self, value=None):
        self._value = value

    def get_phone_number(self, n=5):
        number = self._value.split()
        if n >= 11:
            return '+x xxx xxx xxx'
        k = 1
        for el in reversed(number):
            el = list(el)
            for i in range(1, len(el) + 1):
                if n == 0:
                    break
                el[-i] = 'x'
                n -= 1
                number[-k] = ''.join(el)
            k += 1
        return ' '.join(number)


class Skype:
    def __init__(self, value=None):
        self._value = value

    def get_skype(self):
        if self._value.find('href') > -1:
            return self._value.split(":")[0] + ':xxx?' + self._value.split("?")[1]
        else:
            return self._value.split(":")[0] + ':xxx'
