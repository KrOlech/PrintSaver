from src.python.FilleRead.FileReader import FileReader


def test_readAndSlice():
    fileName = r"Object_1_PLA_5h10m.gcode"

    fileReader = FileReader(fileName)

    fileReader.readFile()

    fileReader.saveFileHigherThan(2, removeHome=True)


test_readAndSlice()
