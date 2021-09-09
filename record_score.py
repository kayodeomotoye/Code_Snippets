class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.ret_list = []
        

    def __call__(self, value):
        self.value = value
        self.ret_list.append(value)
        return max(self.ret_list)
        

#pybites
class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self._score = float('-inf')

    def __call__(self, num):
        self._score = max(self._score, num)
        return self._score