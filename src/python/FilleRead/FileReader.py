from src.python.Leyer.Leyer import Leyer


class FileReader:

    def __init__(self, fileName):
        self.fileName = fileName
        self.layers = []

    def readFile(self):
        with open(self.fileName, "r") as file:
            while line := file.readline():
                if len(line):
                    self.__decodeLine(line)
        [print(line.hight) for line in self.layers]

    def __decodeLine(self, line):
        marker = line[0]
        match marker:
            case ";":
                ...
            case "G":
                self.__decodeGcode(line[1:])
            case "M":
                ...
            case _:
                ...

    def __decodeGcode(self, line):
        try:
            number = int(line[:line.find(" ")])
        except ValueError as e:
            print(e)
            return None

        match number:
            case 1:
                self.__decodeCords(line)

    def __decodeCords(self, line):
        xState = line.find("X")
        yState = line.find("Y")
        zState = line.find("Z")

        match xState, yState, zState:
            case -1, -1, 2:
                self.layers.append(Leyer(line[2:]))

