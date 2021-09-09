from datetime import date, datetime

MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args):
        dict.__init__(self, args)
        self.__dict__ = self

    def __setitem__(self, name, birthday):
        dict.__setitem__(self, name, birthday)
        if (
            len(
                [
                    _date
                    for _date in list(self.values())
                    if datetime.strftime(birthday, "%m-%d") in str(_date)
                ]
            )
            > 1
        ):
            print(MSG.format(name))


#pybites

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):
        has_birthday = any(birthday.strftime('%d/%m') == dt.strftime('%d/%m')
                           for dt in self.values())

        if has_birthday:
            print(MSG.format(name))

        super().__setitem__(name, birthday)