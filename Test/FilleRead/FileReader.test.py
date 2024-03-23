from src.python.FilleRead.FileReader import FileReader


def test_readAndSlice():
    fileName = r"Object_1_PLA_5h10m.gcode"

    fileReader = FileReader(fileName)

    fileReader.readFile()


test_readAndSlice()
