from functools import cache


class Leyer:

    def __init__(self, line: str):
        self.line = line

    @property
    @cache
    def hight(self):
        endSpace = self.line.find(" ")
        try:
            if endSpace > 0:
                return float(self.line[1:endSpace])
            else:
                return float(self.line[1:endSpace])
        except ValueError as e:
            print(e)
            return None

    def __resolveHeight(self):
        ...
