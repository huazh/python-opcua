if __name__ == "__main__":
    inputfile = open("NodeIds.csv")
    outputfile = open("../opcua/ua/object_ids.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    outputfile.write("from enum import IntEnum\n")
    outputfile.write("\n")
    outputfile.write("class ObjectIds(object):\n")
    for line in inputfile:
        name, nb, datatype = line.split(",")
        outputfile.write("    {} = {}\n".format(name, nb))

    inputfile = open("AttributeIds.csv")
    outputfile = open("../opcua/ua/attribute_ids.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    outputfile.write("from enum import IntEnum\n")
    outputfile.write("\n")
    outputfile.write("class AttributeIds(IntEnum):\n")
    for line in inputfile:
        name, nb = line.split(",")
        outputfile.write("    {} = {}\n".format(name.strip(), nb.strip()))

