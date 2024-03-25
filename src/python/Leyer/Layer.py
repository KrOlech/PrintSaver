from functools import cache


class Layer:

    def __init__(self, line: str, lineNumber: int, lastLayerNumber: int):
        self.line = line
        self.lineNumber = lineNumber
        self.lastLayerNumber = lastLayerNumber

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

    def __str__(self):
        return f"{self.hight} {self.lastLayerNumber}-{self.lineNumber}"
