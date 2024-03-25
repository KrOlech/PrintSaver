from src.python.Leyer.Layer import Layer


class FileReader:

    def __init__(self, fileName):
        self.fileName = fileName
        self.layers = []
        self.homingLocations = []
        self.currentLine = 0
        self.lastLayerChange = 0

    def readFile(self):
        with open(self.fileName, "r") as file:
            while line := file.readline():
                self.currentLine += 1
                if len(line):
                    self.__decodeLine(line)

        endHight = f'{self.layers[-1].hight}\n'
        self.layers.append(Layer(endHight, self.currentLine, self.lastLayerChange))

        self.__resolveHeightFromLayer()

    def __resolveHeightFromLayer(self):
        self.heightFromLayer = []
        for layer in self.layers:
            for _ in range(layer.lineNumber - layer.lastLayerNumber):
                self.heightFromLayer.append(layer.hight)

    def saveFileHigherThan(self, hight, newName=None, removeHome=False):
        if not newName:
            newName = "resc_" + self.fileName

        with open(self.fileName, "r") as file, open(newName, "w") as newFile:
            for lineNumber, currentHeight in enumerate(self.heightFromLayer):
                line = file.readline()
                isHomingLine = lineNumber+1 in self.homingLocations
                if isHomingLine:
                    print(line)

                if currentHeight > hight and not (isHomingLine and removeHome):
                    newFile.write(line)
                    # print(lineNumber, currentHeight)

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
            case 28:  # home All axis
                self.homingLocations.append(self.currentLine)

    def __decodeCords(self, line):
        xState = line.find("X")
        yState = line.find("Y")
        zState = line.find("Z")

        match xState, yState, zState:
            case -1, -1, 2:
                self.layers.append(Layer(line[2:], self.currentLine, self.lastLayerChange))
                self.lastLayerChange = self.currentLine
