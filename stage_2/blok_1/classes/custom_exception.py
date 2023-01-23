
class MyException(Exception):
    msg = "to moj message, nazwa: {}, działanie {}"

    def __init__(self, nazwa, dzialanie):
        self.nazwa = nazwa
        self.dzialanie = dzialanie

        msg = MyException.msg.format(self.nazwa, self.dzialanie)

        super().__init__(msg)


try:
    raise MyException("NAZWA", "JAKIES DZIALANIE")
except MyException as e:
    print(f"msg: {e}")
    print(f"nazwa: {e.nazwa}, dzialanie: {e.dzialanie}")


############################################

class HeightOutOfRangeException(Exception):
    def __init__(self):
        super().__init__('Wzrost poza zakresem')


def bmi(m, w):
    if w < 0.2 or w > 2.5:
        raise HeightOutOfRangeException
    return round(m / pow(w, 2), 2)


print(bmi(80, 176))
